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
from tencentcloud.essbasic.v20210526 import models


class EssbasicClient(AbstractClient):
    _apiVersion = '2021-05-26'
    _endpoint = 'essbasic.tencentcloudapi.com'
    _service = 'essbasic'


    def ChannelBatchCancelFlows(self, request):
        """指定需要批量撤销的签署流程Id，批量撤销合同
        客户指定需要撤销的签署流程Id，最多100个，超过100不处理；

        可以撤回：未全部签署完成
         不可以撤回：已全部签署完成、已拒签、已过期、已撤回、拒绝填写、已解除等合同状态。

        **满足撤销条件的合同会发起异步撤销流程，不满足撤销条件的合同返回失败原因。**

        **合同撤销成功后，会通过合同状态为 CANCEL 的回调消息通知调用方 [具体可参考回调消息](https://qian.tencent.com/developers/scenes/partner/callback_data_types#-%E5%90%88%E5%90%8C%E7%8A%B6%E6%80%81%E9%80%9A%E7%9F%A5---flowstatuschange)**

        **注意:
        能撤回合同的只能是合同的发起人或者发起企业的超管、法人**

        :param request: Request instance for ChannelBatchCancelFlows.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.ChannelBatchCancelFlowsRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.ChannelBatchCancelFlowsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ChannelBatchCancelFlows", params, headers=headers)
            response = json.loads(body)
            model = models.ChannelBatchCancelFlowsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ChannelCancelFlow(self, request):
        """撤销签署流程接口，可以撤回：未全部签署完成；不可以撤回（终态）：已全部签署完成、已拒签、已过期、已撤回。
        注意:
        能撤回合同的只能是合同的发起人或者发起企业的超管、法人

        :param request: Request instance for ChannelCancelFlow.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.ChannelCancelFlowRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.ChannelCancelFlowResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ChannelCancelFlow", params, headers=headers)
            response = json.loads(body)
            model = models.ChannelCancelFlowResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ChannelCancelMultiFlowSignQRCode(self, request):
        """此接口（ChannelCancelMultiFlowSignQRCode）用于取消一码多扫二维码。该接口对传入的二维码ID，若还在有效期内，可以提前失效。

        :param request: Request instance for ChannelCancelMultiFlowSignQRCode.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.ChannelCancelMultiFlowSignQRCodeRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.ChannelCancelMultiFlowSignQRCodeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ChannelCancelMultiFlowSignQRCode", params, headers=headers)
            response = json.loads(body)
            model = models.ChannelCancelMultiFlowSignQRCodeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ChannelCancelUserAutoSignEnableUrl(self, request):
        """此接口（ChannelCancelUserAutoSignEnableUrl）用来撤销发送给个人用户的自动签开通链接，撤销后对应的个人用户开通链接失效。若个人用户已经完成开通，将无法撤销。（处方单场景专用，使用此接口请与客户经理确认）

        :param request: Request instance for ChannelCancelUserAutoSignEnableUrl.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.ChannelCancelUserAutoSignEnableUrlRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.ChannelCancelUserAutoSignEnableUrlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ChannelCancelUserAutoSignEnableUrl", params, headers=headers)
            response = json.loads(body)
            model = models.ChannelCancelUserAutoSignEnableUrlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ChannelCreateBatchCancelFlowUrl(self, request):
        """指定需要批量撤销的签署流程Id，获取批量撤销链接 - 不建议使用此接口，可使用ChannelBatchCancelFlows
        客户指定需要撤销的签署流程Id，最多100个，超过100不处理；
        接口调用成功返回批量撤销合同的链接，通过链接跳转到电子签小程序完成批量撤销;

        可以撤回：未全部签署完成
         不可以撤回：已全部签署完成、已拒签、已过期、已撤回、拒绝填写、已解除等合同状态。

        注意:
        能撤回合同的只能是合同的发起人或者发起企业的超管、法人

        :param request: Request instance for ChannelCreateBatchCancelFlowUrl.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.ChannelCreateBatchCancelFlowUrlRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.ChannelCreateBatchCancelFlowUrlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ChannelCreateBatchCancelFlowUrl", params, headers=headers)
            response = json.loads(body)
            model = models.ChannelCreateBatchCancelFlowUrlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ChannelCreateBatchSignUrl(self, request):
        """通过此接口，创建小程序批量签署链接，个人/企业员工点击此链接即可跳转小程序进行批量签署。
        请确保生成链接时候的身份信息和签署合同参与方的信息保持一致。

        注：
        - 参与人点击链接后需短信验证码才能查看合同内容。
        - 企业用户批量签署，需要传OrganizationName（参与方所在企业名称）参数生成签署链接，`请确保此企业已完成腾讯电子签企业认证`。
        - 个人批量签署，签名区`仅支持手写签名`。

        :param request: Request instance for ChannelCreateBatchSignUrl.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.ChannelCreateBatchSignUrlRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.ChannelCreateBatchSignUrlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ChannelCreateBatchSignUrl", params, headers=headers)
            response = json.loads(body)
            model = models.ChannelCreateBatchSignUrlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ChannelCreateBoundFlows(self, request):
        """此接口（ChannelCreateBoundFlows）用于子客领取合同，经办人需要有相应的角色，合同不能重复领取。

        :param request: Request instance for ChannelCreateBoundFlows.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.ChannelCreateBoundFlowsRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.ChannelCreateBoundFlowsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ChannelCreateBoundFlows", params, headers=headers)
            response = json.loads(body)
            model = models.ChannelCreateBoundFlowsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ChannelCreateConvertTaskApi(self, request):
        """上传了word、excel、图片文件后，通过该接口发起文件转换任务，将word、excel、图片文件转换为pdf文件。

        :param request: Request instance for ChannelCreateConvertTaskApi.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.ChannelCreateConvertTaskApiRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.ChannelCreateConvertTaskApiResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ChannelCreateConvertTaskApi", params, headers=headers)
            response = json.loads(body)
            model = models.ChannelCreateConvertTaskApiResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ChannelCreateEmbedWebUrl(self, request):
        """本接口（ChannelCreateEmbedWebUrl）用于创建常规模块嵌入web的链接
        本接口支持创建：创建印章，创建模板，修改模板，预览模板，预览合同流程的web链接
        进入web连接后与当前控制台操作保持一致

        :param request: Request instance for ChannelCreateEmbedWebUrl.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.ChannelCreateEmbedWebUrlRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.ChannelCreateEmbedWebUrlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ChannelCreateEmbedWebUrl", params, headers=headers)
            response = json.loads(body)
            model = models.ChannelCreateEmbedWebUrlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ChannelCreateFlowApprovers(self, request):
        """适用场景：
        当通过模板或文件发起合同时，若未指定企业签署人信息，则可调用此接口动态补充签署人。同一签署人只允许补充一人，最终实际签署人取决于谁先领取合同完成签署。

        限制条件：
        1. 本企业（发起方企业）企业签署人仅支持通过企业名称+姓名+手机号进行补充。
        2. 个人签署人仅支持通过姓名+手机号进行补充。

        :param request: Request instance for ChannelCreateFlowApprovers.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.ChannelCreateFlowApproversRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.ChannelCreateFlowApproversResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ChannelCreateFlowApprovers", params, headers=headers)
            response = json.loads(body)
            model = models.ChannelCreateFlowApproversResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ChannelCreateFlowByFiles(self, request):
        """接口（ChannelCreateFlowByFiles）用PDF文件创建签署流程。

        注: `此接口静默签(企业自动签)能力为白名单功能，使用前请联系对接的客户经理沟通。`

        :param request: Request instance for ChannelCreateFlowByFiles.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.ChannelCreateFlowByFilesRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.ChannelCreateFlowByFilesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ChannelCreateFlowByFiles", params, headers=headers)
            response = json.loads(body)
            model = models.ChannelCreateFlowByFilesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ChannelCreateFlowGroupByFiles(self, request):
        """接口（ChannelCreateFlowGroupByFiles）用于通过多文件创建合同组签署流程。

        :param request: Request instance for ChannelCreateFlowGroupByFiles.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.ChannelCreateFlowGroupByFilesRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.ChannelCreateFlowGroupByFilesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ChannelCreateFlowGroupByFiles", params, headers=headers)
            response = json.loads(body)
            model = models.ChannelCreateFlowGroupByFilesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ChannelCreateFlowGroupByTemplates(self, request):
        """接口（ChannelCreateFlowGroupByTemplates）用于通过多模板创建合同组签署流程。

        :param request: Request instance for ChannelCreateFlowGroupByTemplates.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.ChannelCreateFlowGroupByTemplatesRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.ChannelCreateFlowGroupByTemplatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ChannelCreateFlowGroupByTemplates", params, headers=headers)
            response = json.loads(body)
            model = models.ChannelCreateFlowGroupByTemplatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ChannelCreateFlowReminds(self, request):
        """指定需要批量催办的签署流程Id，批量催办合同，最多100个；接口失败后返回错误信息
        注意:
        该接口不可直接调用，请联系客户经理申请使用
        仅能催办当前状态为“待签署”的签署人，且只能催办一次

        :param request: Request instance for ChannelCreateFlowReminds.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.ChannelCreateFlowRemindsRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.ChannelCreateFlowRemindsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ChannelCreateFlowReminds", params, headers=headers)
            response = json.loads(body)
            model = models.ChannelCreateFlowRemindsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ChannelCreateFlowSignReview(self, request):
        """提交企业流程审批结果
        目前存在两种审核操作，签署审核，发起审核
        签署审核：通过接口（CreateFlowsByTemplates或ChannelCreateFlowByFiles或ChannelCreatePrepareFlow）发起签署流程后，若指定了参数 NeedSignReview 为true,则可以调用此接口，指定operate=SignReview，提交企业内部签署审批结果；若签署流程状态正常，且本企业存在签署方未签署，同一签署流程可以多次提交签署审批结果，签署时的最后一个“审批结果”有效

        发起审核：通过接口ChannelCreatePrepareFlow指定发起后需要审核，则可以通过调用此接口，指定operate=CreateReview，提交企业内部审批结果，可多次提交，当通过后，后续提交结果无效

        :param request: Request instance for ChannelCreateFlowSignReview.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.ChannelCreateFlowSignReviewRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.ChannelCreateFlowSignReviewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ChannelCreateFlowSignReview", params, headers=headers)
            response = json.loads(body)
            model = models.ChannelCreateFlowSignReviewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ChannelCreateFlowSignUrl(self, request):
        """创建个人签署H5签署链接，请联系客户经理申请使用<br/>
        该接口用于发起合同后，生成C端签署人的签署链接<br/>
        注意：该接口目前签署人类型仅支持个人签署方（PERSON）<br/>
        注意：该接口可生成签署链接的C端签署人必须仅有手写签名和时间类型的签署控件<br/>
        注意：该接口返回的签署链接是用于APP集成的场景，支持APP打开或浏览器直接打开，不支持微信小程序嵌入。微信小程序请使用小程序跳转或半屏弹窗的方式<br/>

        :param request: Request instance for ChannelCreateFlowSignUrl.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.ChannelCreateFlowSignUrlRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.ChannelCreateFlowSignUrlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ChannelCreateFlowSignUrl", params, headers=headers)
            response = json.loads(body)
            model = models.ChannelCreateFlowSignUrlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ChannelCreateMultiFlowSignQRCode(self, request):
        """此接口（ChannelCreateMultiFlowSignQRCode）用于创建一码多扫流程签署二维码。 适用场景：无需填写签署人信息，可通过模板id生成签署二维码，签署人可通过扫描二维码补充签署信息进行实名签署。常用于提前不知道签署人的身份信息场景，例如：劳务工招工、大批量员工入职等场景。

        **本接口适用于发起方没有填写控件的 B2C或者单C模板**

        **若是B2C模板,还要满足以下任意一个条件**

        - 模板中配置的签署顺序是无序
        - B端企业的签署方式是静默签署
        - B端企业是非首位签署

        通过一码多扫二维码发起的合同，合同涉及到的回调消息可参考文档[合同发起及签署相关回调
        ]( https://qian.tencent.com/developers/partner/callback_types_contracts_sign)

        用户通过签署二维码发起合同时，因企业额度不足导致失败 会触发签署二维码相关回调,具体参考文档[签署二维码相关回调](https://qian.tencent.com/developers/partner/callback_types_commons#%E7%AD%BE%E7%BD%B2%E4%BA%8C%E7%BB%B4%E7%A0%81%E7%9B%B8%E5%85%B3%E5%9B%9E%E8%B0%83)

        :param request: Request instance for ChannelCreateMultiFlowSignQRCode.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.ChannelCreateMultiFlowSignQRCodeRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.ChannelCreateMultiFlowSignQRCodeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ChannelCreateMultiFlowSignQRCode", params, headers=headers)
            response = json.loads(body)
            model = models.ChannelCreateMultiFlowSignQRCodeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ChannelCreateOrganizationBatchSignUrl(self, request):
        """通过此接口，创建小程序批量签署链接，可以创建企业批量签署链接，员工只需点击链接即可跳转至控制台进行批量签署。

        注：
        - 员工必须在企业下完成实名认证，且需作为批量签署合同的签署方或者领取方。
        - 仅支持传入待签署或者待领取的合同，待填写暂不支持。
        - 员工批量签署，支持多种签名方式，包括手写签名、临摹签名、系统签名、个人印章，暂不支持签批控件

        :param request: Request instance for ChannelCreateOrganizationBatchSignUrl.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.ChannelCreateOrganizationBatchSignUrlRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.ChannelCreateOrganizationBatchSignUrlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ChannelCreateOrganizationBatchSignUrl", params, headers=headers)
            response = json.loads(body)
            model = models.ChannelCreateOrganizationBatchSignUrlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ChannelCreateOrganizationModifyQrCode(self, request):
        """生成渠道子客编辑企业信息二维码

        :param request: Request instance for ChannelCreateOrganizationModifyQrCode.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.ChannelCreateOrganizationModifyQrCodeRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.ChannelCreateOrganizationModifyQrCodeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ChannelCreateOrganizationModifyQrCode", params, headers=headers)
            response = json.loads(body)
            model = models.ChannelCreateOrganizationModifyQrCodeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ChannelCreatePrepareFlow(self, request):
        """创建预发起合同
        通过此接口指定：合同，签署人，填写控件信息，生成预创建合同链接，点击后跳转到web页面完成合同创建并发起
        可指定合同信息不可更改，签署人信息不可更改
        合同发起后，填写及签署流程与现有操作流程一致
        注意：目前仅支持模板发起

        :param request: Request instance for ChannelCreatePrepareFlow.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.ChannelCreatePrepareFlowRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.ChannelCreatePrepareFlowResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ChannelCreatePrepareFlow", params, headers=headers)
            response = json.loads(body)
            model = models.ChannelCreatePrepareFlowResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ChannelCreatePreparedPersonalEsign(self, request):
        """本接口（ChannelCreatePreparedPersonalEsign）用于创建导入个人印章（处方单场景专用，使用此接口请与客户经理确认）。

        :param request: Request instance for ChannelCreatePreparedPersonalEsign.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.ChannelCreatePreparedPersonalEsignRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.ChannelCreatePreparedPersonalEsignResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ChannelCreatePreparedPersonalEsign", params, headers=headers)
            response = json.loads(body)
            model = models.ChannelCreatePreparedPersonalEsignResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ChannelCreateReleaseFlow(self, request):
        """发起解除协议，主要应用场景为：基于一份已经签署的合同，进行解除操作。
        合同发起人必须在电子签已经进行实名。

        :param request: Request instance for ChannelCreateReleaseFlow.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.ChannelCreateReleaseFlowRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.ChannelCreateReleaseFlowResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ChannelCreateReleaseFlow", params, headers=headers)
            response = json.loads(body)
            model = models.ChannelCreateReleaseFlowResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ChannelCreateRole(self, request):
        """此接口（ChannelCreateRole）用来创建企业自定义角色。

        适用场景1：创建当前企业的自定义角色，并且创建时不进行权限的设置（PermissionGroups 参数不传），角色中的权限内容可通过接口 ChannelModifyRole 完成更新。

        适用场景2：创建当前企业的自定义角色，并且创建时进行权限的设置（PermissionGroups 参数要传），权限树内容 PermissionGroups 可参考接口 ChannelDescribeRoles 的输出。此处注意权限树内容可能会更新，需尽量拉取最新的权限树内容，并且权限树内容 PermissionGroups 必须是一颗完整的权限树。

        :param request: Request instance for ChannelCreateRole.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.ChannelCreateRoleRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.ChannelCreateRoleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ChannelCreateRole", params, headers=headers)
            response = json.loads(body)
            model = models.ChannelCreateRoleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ChannelCreateSealPolicy(self, request):
        """将指定印章授权给第三方平台子客企业下的某些员工

        :param request: Request instance for ChannelCreateSealPolicy.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.ChannelCreateSealPolicyRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.ChannelCreateSealPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ChannelCreateSealPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.ChannelCreateSealPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ChannelCreateUserAutoSignEnableUrl(self, request):
        """企业方可以通过此接口获取个人用户开启自动签的跳转链接

        :param request: Request instance for ChannelCreateUserAutoSignEnableUrl.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.ChannelCreateUserAutoSignEnableUrlRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.ChannelCreateUserAutoSignEnableUrlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ChannelCreateUserAutoSignEnableUrl", params, headers=headers)
            response = json.loads(body)
            model = models.ChannelCreateUserAutoSignEnableUrlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ChannelCreateUserAutoSignSealUrl(self, request):
        """获取设置自动签印章小程序链接。

        注意：
        <ul><li>需要<code>企业开通自动签</code>后使用。</li>
        <li>仅支持<code>已经开通了自动签的个人</code>更换自动签印章。</li>
        <li>链接有效期默认7天，<code>最多30天</code>。</li>
        <li>该接口的链接适用于<code>小程序</code>端。</li>
        <li>该接口不会扣除您的合同套餐，暂不参与计费。</li></ul>

        :param request: Request instance for ChannelCreateUserAutoSignSealUrl.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.ChannelCreateUserAutoSignSealUrlRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.ChannelCreateUserAutoSignSealUrlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ChannelCreateUserAutoSignSealUrl", params, headers=headers)
            response = json.loads(body)
            model = models.ChannelCreateUserAutoSignSealUrlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ChannelCreateUserRoles(self, request):
        """通过此接口，绑定员工角色，支持以电子签userId、客户系统userId两种方式调用。

        :param request: Request instance for ChannelCreateUserRoles.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.ChannelCreateUserRolesRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.ChannelCreateUserRolesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ChannelCreateUserRoles", params, headers=headers)
            response = json.loads(body)
            model = models.ChannelCreateUserRolesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ChannelCreateWebThemeConfig(self, request):
        """用来创建嵌入式页面个性化主题配置（例如是否展示电子签logo、定义主题色等），该接口配合其他所有可嵌入页面接口使用
        创建配置对当前第三方应用全局生效，如果多次调用，会以最后一次的配置为准

        :param request: Request instance for ChannelCreateWebThemeConfig.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.ChannelCreateWebThemeConfigRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.ChannelCreateWebThemeConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ChannelCreateWebThemeConfig", params, headers=headers)
            response = json.loads(body)
            model = models.ChannelCreateWebThemeConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ChannelDeleteRole(self, request):
        """此接口（ChannelDeleteRole）用来删除企业自定义角色。

        注意：系统角色不可删除。

        :param request: Request instance for ChannelDeleteRole.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.ChannelDeleteRoleRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.ChannelDeleteRoleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ChannelDeleteRole", params, headers=headers)
            response = json.loads(body)
            model = models.ChannelDeleteRoleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ChannelDeleteRoleUsers(self, request):
        """通过此接口，删除员工绑定的角色，支持以电子签userId、客户系统userId两种方式调用。

        :param request: Request instance for ChannelDeleteRoleUsers.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.ChannelDeleteRoleUsersRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.ChannelDeleteRoleUsersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ChannelDeleteRoleUsers", params, headers=headers)
            response = json.loads(body)
            model = models.ChannelDeleteRoleUsersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ChannelDeleteSealPolicies(self, request):
        """删除指定印章下多个授权信息

        :param request: Request instance for ChannelDeleteSealPolicies.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.ChannelDeleteSealPoliciesRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.ChannelDeleteSealPoliciesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ChannelDeleteSealPolicies", params, headers=headers)
            response = json.loads(body)
            model = models.ChannelDeleteSealPoliciesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ChannelDescribeEmployees(self, request):
        """查询企业员工列表

        :param request: Request instance for ChannelDescribeEmployees.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.ChannelDescribeEmployeesRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.ChannelDescribeEmployeesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ChannelDescribeEmployees", params, headers=headers)
            response = json.loads(body)
            model = models.ChannelDescribeEmployeesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ChannelDescribeFlowComponents(self, request):
        """查询流程填写控件内容，可以根据流程Id查询该流程相关联的填写控件信息和填写内容。 注意：使用此接口前，需要在【企业应用管理】-【应用集成】-【第三方应用管理】中开通【下载应用内全量合同文件及内容数据】功能。

        :param request: Request instance for ChannelDescribeFlowComponents.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.ChannelDescribeFlowComponentsRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.ChannelDescribeFlowComponentsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ChannelDescribeFlowComponents", params, headers=headers)
            response = json.loads(body)
            model = models.ChannelDescribeFlowComponentsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ChannelDescribeOrganizationSeals(self, request):
        """查询子客企业电子印章，需要操作者具有管理印章权限
        客户指定需要获取的印章数量和偏移量，数量最多100，超过100按100处理；入参InfoType控制印章是否携带授权人信息，为1则携带，为0则返回的授权人信息为空数组。接口调用成功返回印章的信息列表还有企业印章的总数，只返回启用的印章。

        :param request: Request instance for ChannelDescribeOrganizationSeals.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.ChannelDescribeOrganizationSealsRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.ChannelDescribeOrganizationSealsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ChannelDescribeOrganizationSeals", params, headers=headers)
            response = json.loads(body)
            model = models.ChannelDescribeOrganizationSealsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ChannelDescribeRoles(self, request):
        """分页查询企业角色列表，法人的角色是系统保留角色，不会返回，按照角色创建时间升序排列。
        相关系统默认角色说明可参考文档：https://cloud.tencent.com/document/product/1323/61355

        :param request: Request instance for ChannelDescribeRoles.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.ChannelDescribeRolesRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.ChannelDescribeRolesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ChannelDescribeRoles", params, headers=headers)
            response = json.loads(body)
            model = models.ChannelDescribeRolesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ChannelDescribeUserAutoSignStatus(self, request):
        """企业方可以通过此接口查询个人用户自动签开启状态

        :param request: Request instance for ChannelDescribeUserAutoSignStatus.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.ChannelDescribeUserAutoSignStatusRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.ChannelDescribeUserAutoSignStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ChannelDescribeUserAutoSignStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ChannelDescribeUserAutoSignStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ChannelDisableUserAutoSign(self, request):
        """企业方可以通过此接口关闭个人的自动签功能

        :param request: Request instance for ChannelDisableUserAutoSign.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.ChannelDisableUserAutoSignRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.ChannelDisableUserAutoSignResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ChannelDisableUserAutoSign", params, headers=headers)
            response = json.loads(body)
            model = models.ChannelDisableUserAutoSignResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ChannelGetTaskResultApi(self, request):
        """查询转换任务的状态。转换任务Id通过发起转换任务接口（ChannelCreateConvertTaskApi）获取。
        注意：大文件转换所需的时间可能会比较长。

        :param request: Request instance for ChannelGetTaskResultApi.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.ChannelGetTaskResultApiRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.ChannelGetTaskResultApiResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ChannelGetTaskResultApi", params, headers=headers)
            response = json.loads(body)
            model = models.ChannelGetTaskResultApiResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ChannelModifyRole(self, request):
        """此接口（ChannelModifyRole）用来更新企业自定义角色。

        适用场景1：更新当前企业的自定义角色的名称或描述等其他信息，更新时不进行权限的设置（PermissionGroups 参数不传）。

        适用场景2：更新当前企业的自定义角色的权限信息，更新时进行权限的设置（PermissionGroups 参数要传），权限树内容 PermissionGroups 可参考接口 ChannelDescribeRoles 的输出。此处注意权限树内容可能会更新，需尽量拉取最新的权限树内容，并且权限树内容 PermissionGroups 必须是一颗完整的权限树。

        :param request: Request instance for ChannelModifyRole.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.ChannelModifyRoleRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.ChannelModifyRoleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ChannelModifyRole", params, headers=headers)
            response = json.loads(body)
            model = models.ChannelModifyRoleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ChannelUpdateSealStatus(self, request):
        """本接口（ChannelUpdateSealStatus）用于第三方应用平台为子客企业更新印章状态

        :param request: Request instance for ChannelUpdateSealStatus.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.ChannelUpdateSealStatusRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.ChannelUpdateSealStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ChannelUpdateSealStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ChannelUpdateSealStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ChannelVerifyPdf(self, request):
        """对流程的合同文件进行数字签名验证，判断文件是否被篡改。

        :param request: Request instance for ChannelVerifyPdf.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.ChannelVerifyPdfRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.ChannelVerifyPdfResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ChannelVerifyPdf", params, headers=headers)
            response = json.loads(body)
            model = models.ChannelVerifyPdfResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateChannelFlowEvidenceReport(self, request):
        """创建出证报告，返回报告 ID。需要配合出证套餐才能调用。
        出证需要一定时间，建议调用创建出证24小时之后再通过DescribeChannelFlowEvidenceReport进行查询。

        :param request: Request instance for CreateChannelFlowEvidenceReport.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.CreateChannelFlowEvidenceReportRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.CreateChannelFlowEvidenceReportResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateChannelFlowEvidenceReport", params, headers=headers)
            response = json.loads(body)
            model = models.CreateChannelFlowEvidenceReportResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateChannelOrganizationInfoChangeUrl(self, request):
        """此接口（CreateChannelOrganizationInfoChangeUrl）用于创建子客企业信息变更链接，支持创建企业超管变更链接或企业基础信息变更链接，通过入参ChangeType指定。

        :param request: Request instance for CreateChannelOrganizationInfoChangeUrl.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.CreateChannelOrganizationInfoChangeUrlRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.CreateChannelOrganizationInfoChangeUrlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateChannelOrganizationInfoChangeUrl", params, headers=headers)
            response = json.loads(body)
            model = models.CreateChannelOrganizationInfoChangeUrlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateConsoleLoginUrl(self, request):
        """此接口（CreateConsoleLoginUrl）用于创建第三方平台子客企业控制台Web/移动登录链接。支持web控制台、电子签小程序和H5链接。登录链接是进入子客控制台的唯一入口。
        链接访问后，会根据企业的和员工的状态（企业根据ProxyOrganizationOpenId参数，员工根据OpenId参数判断），进入不同的流程，主要情况分类如下：
        1. 若子客企业未激活，会进入企业激活流程，首次参与激活流程的经办人会成为超管。
        2. 若子客企业已激活，员工未激活，则会进入经办人激活流程。
        3. 若子客企业、经办人均已完成认证，则会直接进入子客Web控制台。

        如果是企业激活流程，需要注意如下情况：

        1. 若在激活过程中，更换用户OpenID重新生成链接，之前的认证会被清理。因此不要在认证过程中多人同时操作，导致认证过程互相影响。
        2. 若您认证中发现信息有误需要重新认证，可以通过更换OpenID重新生成链接的方式，来清理掉已有的流程。

        :param request: Request instance for CreateConsoleLoginUrl.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.CreateConsoleLoginUrlRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.CreateConsoleLoginUrlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateConsoleLoginUrl", params, headers=headers)
            response = json.loads(body)
            model = models.CreateConsoleLoginUrlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateFlowsByTemplates(self, request):
        """接口（CreateFlowsByTemplates）用于使用模板批量创建签署流程。当前可批量发起合同（签署流程）数量为1-20个。
        如若在模板中配置了动态表格, 上传的附件必须为A4大小
        合同发起人必须在电子签已经进行实名。

        :param request: Request instance for CreateFlowsByTemplates.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.CreateFlowsByTemplatesRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.CreateFlowsByTemplatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateFlowsByTemplates", params, headers=headers)
            response = json.loads(body)
            model = models.CreateFlowsByTemplatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSealByImage(self, request):
        """通过图片为子客企业代创建印章，图片最大5MB

        :param request: Request instance for CreateSealByImage.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.CreateSealByImageRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.CreateSealByImageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSealByImage", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSealByImageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSignUrls(self, request):
        """创建跳转小程序查看或签署的链接。

        跳转小程序的几种方式：主要是设置不同的EndPoint
        1. 通过链接Url直接跳转到小程序，不需要返回
        设置EndPoint为WEIXINAPP，得到链接打开即可。（与短信提醒用户签署形式一样）。

        2. 通过链接Url打开H5引导页-->点击跳转到小程序-->签署完退出小程序-->回到H5引导页-->跳转到指定JumpUrl
        设置EndPoint为CHANNEL，指定JumpUrl，得到链接打开即可。

        3. 客户App直接跳转到小程序-->小程序签署完成-->返回App
        跳转到小程序的实现，参考官方文档
        https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/launchApp.html
        其中小程序的原始Id，请联系<对接技术人员>获取，或者查看小程序信息自助获取。
        使用CreateSignUrls，设置EndPoint为APP，得到path。

        4. 客户小程序直接跳到电子签小程序-->签署完成退出电子签小程序-->回到客户小程序
        跳转到小程序的实现，参考官方文档（分为全屏、半屏两种方式）
        全屏方式：
        （https://developers.weixin.qq.com/miniprogram/dev/api/navigate/wx.navigateToMiniProgram.html ）
        半屏方式：
        （https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/openEmbeddedMiniProgram.html ）
        其中小程序的原始Id，请联系<对接技术人员>获取，或者查看小程序信息自助获取。
        使用CreateSignUrls，设置EndPoint为APP，得到path。

        其中小程序的原始Id如下，或者查看小程序信息自助获取。

        | 小程序 | AppID | 原始ID |
        | ------------ | ------------ | ------------ |
        | 腾讯电子签（正式版） | wxa023b292fd19d41d | gh_da88f6188665 |
        | 腾讯电子签Demo | wx371151823f6f3edf | gh_39a5d3de69fa |

        :param request: Request instance for CreateSignUrls.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.CreateSignUrlsRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.CreateSignUrlsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSignUrls", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSignUrlsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeChannelFlowEvidenceReport(self, request):
        """查询出证报告，返回报告 URL。

        :param request: Request instance for DescribeChannelFlowEvidenceReport.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.DescribeChannelFlowEvidenceReportRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.DescribeChannelFlowEvidenceReportResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeChannelFlowEvidenceReport", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeChannelFlowEvidenceReportResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeExtendedServiceAuthInfo(self, request):
        """查询企业扩展服务授权信息，企业经办人需要是企业超管或者法人

        :param request: Request instance for DescribeExtendedServiceAuthInfo.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.DescribeExtendedServiceAuthInfoRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.DescribeExtendedServiceAuthInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeExtendedServiceAuthInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeExtendedServiceAuthInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeFlowDetailInfo(self, request):
        """此接口（DescribeFlowDetailInfo）用于查询合同(签署流程)的详细信息。

        :param request: Request instance for DescribeFlowDetailInfo.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.DescribeFlowDetailInfoRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.DescribeFlowDetailInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFlowDetailInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFlowDetailInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeResourceUrlsByFlows(self, request):
        """根据签署流程信息批量获取资源下载链接，可以下载签署中、签署完的合同，需合作企业先进行授权。
        此接口直接返回下载的资源的url，与接口GetDownloadFlowUrl跳转到控制台的下载方式不同。

        :param request: Request instance for DescribeResourceUrlsByFlows.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.DescribeResourceUrlsByFlowsRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.DescribeResourceUrlsByFlowsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeResourceUrlsByFlows", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeResourceUrlsByFlowsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTemplates(self, request):
        """通过此接口（DescribeTemplates）查询该第三方平台子客企业在电子签拥有的有效模板，不包括第三方平台模板。

        > **适用场景**
        >
        >  该接口常用来配合“使用模板创建签署流程”接口作为前置的接口使用。
        >  一个模板通常会包含以下结构信息
        >- 模板基本信息
        >- 发起方参与信息Promoter、签署参与方 Recipients，后者会在模板发起合同时用于指定参与方
        >- 填写控件 Components
        >- 签署控件 SignComponents
        >- 生成模板的文件基础信息 FileInfos

        :param request: Request instance for DescribeTemplates.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.DescribeTemplatesRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.DescribeTemplatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTemplates", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTemplatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUsage(self, request):
        """此接口（DescribeUsage）用于获取第三方平台所有合作企业流量消耗情况。
         注: 此接口每日限频50次，若要扩大限制次数,请提前与客服经理或邮件至e-contract@tencent.com进行联系。

        :param request: Request instance for DescribeUsage.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.DescribeUsageRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.DescribeUsageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUsage", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUsageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetDownloadFlowUrl(self, request):
        """此接口（GetDownloadFlowUrl）用于创建电子签批量下载地址，让合作企业进入控制台直接下载，支持客户合同（流程）按照自定义文件夹形式 分类下载。
        当前接口限制最多合同（流程）50个.
        返回的链接只能使用一次

        :param request: Request instance for GetDownloadFlowUrl.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.GetDownloadFlowUrlRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.GetDownloadFlowUrlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetDownloadFlowUrl", params, headers=headers)
            response = json.loads(body)
            model = models.GetDownloadFlowUrlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyExtendedService(self, request):
        """修改（操作）企业扩展服务 ，企业经办人需要是企业超管或者法人。

        跳转小程序的几种方式：主要是设置不同的EndPoint
        1. 通过链接Url直接跳转到小程序，不需要返回
        设置EndPoint为WEIXINAPP，得到链接打开即可。

        2. 客户App直接跳转到小程序-->腾讯电子签小程序操作完成-->返回App
        跳转到小程序的实现，参考官方文档
        https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/launchApp.html
        其中小程序的原始Id，请联系<对接技术人员>获取，或者查看小程序信息自助获取。
        设置EndPoint为APP，得到path。

        4. 客户小程序直接跳到电子签小程序-->腾讯电子签小程序操作完成--->回到客户小程序
        跳转到小程序的实现，参考官方文档（分为全屏、半屏两种方式）
        全屏方式：
        （https://developers.weixin.qq.com/miniprogram/dev/api/navigate/wx.navigateToMiniProgram.html）
        半屏方式：
        （https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/openEmbeddedMiniProgram.html）
        其中小程序的原始Id，请联系<对接技术人员>获取，或者查看小程序信息自助获取。
        设置EndPoint为APP，得到path。

        其中小程序的原始Id如下，或者查看小程序信息自助获取。

        | 小程序 | AppID | 原始ID |
        | ------------ | ------------ | ------------ |
        | 腾讯电子签（正式版） | wxa023b292fd19d41d | gh_da88f6188665 |
        | 腾讯电子签Demo | wx371151823f6f3edf | gh_39a5d3de69fa |

        :param request: Request instance for ModifyExtendedService.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.ModifyExtendedServiceRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.ModifyExtendedServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyExtendedService", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyExtendedServiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def OperateChannelTemplate(self, request):
        """此接口（OperateChannelTemplate）用于针对第三方应用平台模板库中的模板对子客企业可见性的查询和设置。

        > **使用场景**
        >
        >  1：查询 OperateType=SELECT
        > - 查询第三方应用平台模板库的可见性以及授权的子客列表。
        >
        >  2：修改部分子客授权 OperateType=UPDATE
        > - 对子客企业进行模板库中模板可见性的进行修改操作。
        >- 当模板未发布时，可以修改可见性AuthTag（part/all），当模板发布后，不可做此修改
        > - 若模板已发布且可见性AuthTag是part，可以通过ProxyOrganizationOpenIds增加子客的授权范围。如果是自动领取的模板，增加授权范围后会自动下发。
        >
        >  3：取消部分子客授权 OperateType=DELETE
        > - 对子客企业进行模板库中模板可见性的进行删除操作。
        > - 主要对于手动领取的模板，去除授权后子客在模板库中看不到，就无法再领取了。但是已经领取过成为自有模板的不会同步删除。
        > - 对于自动领取的模板，由于已经下发，更改授权不会影响。
        > - 如果要同步删除子客自有模板库中的模板，请使用OperateType=UPDATE+Available参数处理。

        :param request: Request instance for OperateChannelTemplate.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.OperateChannelTemplateRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.OperateChannelTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("OperateChannelTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.OperateChannelTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def PrepareFlows(self, request):
        """该接口 (PrepareFlows) 用于创建待发起文件
        用户通过该接口进入签署流程发起的确认页面，进行发起信息二次确认， 如果确认则进行正常发起。
        目前该接口只支持B2C，不建议使用，将会废弃。

        :param request: Request instance for PrepareFlows.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.PrepareFlowsRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.PrepareFlowsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("PrepareFlows", params, headers=headers)
            response = json.loads(body)
            model = models.PrepareFlowsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SyncProxyOrganization(self, request):
        """此接口（SyncProxyOrganization）用于同步第三方平台子客企业信息，包括企业名称，企业营业执照，企业统一社会信用代码和法人姓名等，便于子客企业在企业激活过程中无需手动上传营业执照或补充企业信息。注意：
        1. 需要在子客企业激活前调用该接口，如果您的企业已经提交企业信息或者企业已经激活，同步的企业信息将不会生效。
        2. 如果您同时传递了营业执照信息和企业名称等信息，在认证过程中将以营业执照中的企业信息为准，请注意企业信息需要和营业执照信息对应。

        :param request: Request instance for SyncProxyOrganization.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.SyncProxyOrganizationRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.SyncProxyOrganizationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SyncProxyOrganization", params, headers=headers)
            response = json.loads(body)
            model = models.SyncProxyOrganizationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SyncProxyOrganizationOperators(self, request):
        """此接口（SyncProxyOrganizationOperators）用于同步 第三方平台子客企业经办人列表，主要是同步经办人的离职状态。子客Web控制台的组织架构管理，是依赖于第三方应用平台的，无法针对员工做新增/更新/离职等操作。
        若经办人信息有误，或者需要修改，也可以先将之前的经办人做离职操作，然后重新使用控制台链接CreateConsoleLoginUrl让经办人重新实名。

        :param request: Request instance for SyncProxyOrganizationOperators.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.SyncProxyOrganizationOperatorsRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.SyncProxyOrganizationOperatorsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SyncProxyOrganizationOperators", params, headers=headers)
            response = json.loads(body)
            model = models.SyncProxyOrganizationOperatorsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UploadFiles(self, request):
        """此接口（UploadFiles）用于文件上传。
        其中上传的文件，图片类型(png/jpg/jpeg)大小限制为5M，其他大小限制为60M。
        调用时需要设置Domain, 正式环境为 file.ess.tencent.cn。
        代码示例：
        HttpProfile httpProfile = new HttpProfile();
        httpProfile.setEndpoint("file.test.ess.tencent.cn");

        :param request: Request instance for UploadFiles.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.UploadFilesRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.UploadFilesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UploadFiles", params, headers=headers)
            response = json.loads(body)
            model = models.UploadFilesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))