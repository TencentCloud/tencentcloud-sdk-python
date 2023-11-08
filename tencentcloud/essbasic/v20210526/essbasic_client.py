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
        """通过合同编号批量撤销合同，单次最多支持撤销100份合同。

        适用场景：如果某个合同当前**至少还有一方没有签署**，则可通过该接口取消该合同流程。常用于合同发错、内容填错，需要及时撤销的场景。

        - **可撤回合同状态**：未全部签署完成
        - **不撤回合同状态**：已全部签署完成、已拒签、已过期、已撤回、拒绝填写、已解除等合同状态。

        注:
        - 有对应合同撤销权限的人:  <font color='red'>**合同的发起人或者发起人所在企业的超管、法人**</font>
        - 签署完毕的合同需要双方走解除流程将合同作废，可以参考<a href="https://qian.tencent.com/developers/partnerApis/startFlows/ChannelCreateReleaseFlow" target="_blank">发起解除合同流程接口</a>

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
        """撤销签署流程接口

        适用场景：如果某个合同流程当前至少还有一方没有签署，则可通过该接口取消该合同流程。常用于合同发错、内容填错，需要及时撤销的场景。

        - **可撤回合同状态**：未全部签署完成
        - **不撤回合同状态**：已全部签署完成、已拒签、已过期、已撤回、拒绝填写、已解除等合同状态。

        注:
        - 有对应合同撤销权限的人:  <font color='red'>**合同的发起人或者发起人所在企业的超管、法人**</font>
        - 签署完毕的合同需要双方走解除流程将合同作废，可以参考<a href="https://qian.tencent.com/developers/partnerApis/startFlows/ChannelCreateReleaseFlow" target="_blank">发起解除合同流程接口</a>

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
        """此接口（CancelMultiFlowSignQRCode）用于废除一码多扫流程签署二维码。
        该接口所需的二维码ID，源自[创建一码多扫流程签署二维码](https://qian.tencent.com/developers/partnerApis/templates/ChannelCreateMultiFlowSignQRCode)生成的。
        如果该二维码尚处于有效期内，可通过本接口将其设置为失效状态。

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
        """通过合同编号生成批量撤销合同的链接，单次最多支持撤销100份合同,   返回的链接需要有此权限的人<font color='red'>**合同的发起人或者发起人所在企业的超管、法人**</font>在<font color='red'>**手机端**</font>打开,  跳转到腾讯电子签小程序输入撤销原因来进行撤销合同

        适用场景：如果某个合同当前**至少还有一方没有签署**，则可通过该接口取消该合同流程。常用于合同发错、内容填错，需要及时撤销的场景。

        - **可撤回合同状态**：未全部签署完成
        - **不撤回合同状态**：已全部签署完成、已拒签、已过期、已撤回、拒绝填写、已解除等合同状态。

        注:
        - 签署完毕的合同需要双方走解除流程将合同作废，可以参考<a href="https://qian.tencent.com/developers/partnerApis/startFlows/ChannelCreateReleaseFlow" target="_blank">发起解除合同流程接口</a>

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


    def ChannelCreateBatchQuickSignUrl(self, request):
        """该接口用于发起合同后，生成个人用户的批量签署链接, 暂时不支持企业端签署 <br/>
        `注意：`<br/>
        `1. 该接口目前仅支持签署人类型是个人签署方的批量签署场景(ApproverType=PERSON)。` <br/>
        `2. 该接口可生成批量签署链接的C端签署人必须仅有手写签名和时间类型的签署控件，不支持填写控件 。` <br/>
        `3. 请确保C端签署人在批量签署合同中为待签署状态，如需顺序签署请待前一位参与人签署完成后，再创建该C端用户的签署链接。` <br/>
        `4. 该签署链接有效期为30分钟，过期后将失效，如需签署可重新创建批量签署链接 。` <br/>
        `5. 该接口返回的签署链接适用于APP集成的场景，支持APP打开或浏览器直接打开，不支持微信小程序嵌入。`<br/>
        跳转到小程序的实现，参考微信官方文档(分为<a href="https://developers.weixin.qq.com/miniprogram/dev/api/navigate/wx.navigateToMiniProgram.html">全屏</a>、<a href="https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/openEmbeddedMiniProgram.html">半屏</a>两种方式)，如何配置也可以请参考: <a href="https://qian.tencent.com/developers/company/openwxminiprogram">跳转电子签小程序配置</a>

        :param request: Request instance for ChannelCreateBatchQuickSignUrl.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.ChannelCreateBatchQuickSignUrlRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.ChannelCreateBatchQuickSignUrlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ChannelCreateBatchQuickSignUrl", params, headers=headers)
            response = json.loads(body)
            model = models.ChannelCreateBatchQuickSignUrlResponse()
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
        """此接口（ChannelCreateConvertTaskApi）用来将word、excel、html、图片、txt类型文件转换为PDF文件。<br />
        前提条件：源文件已经通过 <a href="https://qian.tencent.com/developers/partnerApis/files/UploadFiles" target="_blank">文件上传接口</a>完成上传，并得到了源文件的资源Id。<br />
        适用场景1：已经上传了一个word文件，希望将该word文件转换成pdf文件后发起合同
        适用场景2：已经上传了一个jpg图片文件，希望将该图片文件转换成pdf文件后发起合同<br />
        转换文件是一个耗时操作，若想查看转换任务是否完成，可以通过<a href="https://qian.tencent.com/developers/partnerApis/files/ChannelGetTaskResultApi" target="_blank">查询转换任务状态</a>接口获取任务状态。<br />
        注:
        1. `支持的文件类型有doc、docx、xls、xlsx、html、jpg、jpeg、png、bmp、txt`
        2. `可通过发起合同时设置预览来检查转换文件是否达到预期效果`

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

        适用场景：适用非制式的合同文件签署，开发者有每个签署流程的PDF，可以通过该接口传入完整的PDF文件及流程信息生成待签署的合同流程。

        **注**:
        <ul>
        <li>此接口静默签(企业自动签)能力为白名单功能，使用前请联系对接的客户经理沟通。</li>
        <li>此接口需要依赖<a href="https://qian.tencent.com/developers/partnerApis/files/UploadFiles" target="_blank">文件上传接口</a>生成pdf资源编号（FileIds）进行使用。整体的逻辑如下图</li>
        </ul>

        ![image](https://dyn.ess.tencent.cn/guide/capi/ChannelCreateFlowByFiles.png)

        **可以作为发起方和签署方的角色列表**
        <table>
        <thead>
        <tr>
        <th>场景编号</th>
        <th>可作为发起方类型</th>
        <th>可作为签署方的类型</th>
        </tr>
        </thead>

        <tbody>
        <tr>
        <td>场景一</td>
        <td>第三方子企业A员工</td>
        <td>第三方子企业A员工</td>
        </tr>

        <tr>
        <td>场景二</td>
        <td>第三方子企业A员工</td>
        <td>第三方子企业B(不指定经办人)</td>
        </tr>

        <tr>
        <td>场景三</td>
        <td>第三方子企业A员工</td>
        <td>第三方子企业B员工</td>
        </tr>

        <tr>
        <td>场景四</td>
        <td>第三方子企业A员工</td>
        <td>个人/自然人</td>
        </tr>

        <tr>
        <td>场景五</td>
        <td>第三方子企业A员工</td>
        <td>SaaS平台企业员工</td>
        </tr>
        </tbody>
        </table>

        **注**:
        `1. 发起合同时候,  作为发起方的第三方子企业A员工的企业和员工必须经过实名, 而作为签署方的第三方子企业A员工/个人/自然人/SaaS平台企业员工/第三方子企业B员工企业中的企业和个人/员工可以未实名`
        `2. 不同类型的签署方传参不同, 可以参考开发者中心的FlowApproverInfo结构体说明`

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
        """接口（ChannelCreateFlowGroupByFiles）用于使用 PDF 文件创建合同组签署流程。

        合同组是将多个合同签署流程组织在一起，多个合同同时创建，每个签署方得到一个签署链接，`一次完成合同组中多个合同的签署`。合同组的合同`不能拆分一个一个签署`，只能作为一个整体签署。

        适用场景：该接口适用于需要一次性完成多份合同签署的情况，多份合同一般具有关联性，用户以目录的形式查看合同。



        **注**:
        <ul>
        <li>此接口静默签(企业自动签)能力为白名单功能，使用前请联系对接的客户经理沟通。</li>
        <li>合同组暂不支持抄送功能</li>
        <li>此接口需要依赖<a href="https://qian.tencent.com/developers/partnerApis/files/UploadFiles" target="_blank">文件上传接口</a>生成pdf资源编号（FileIds）进行使用。</li>
        </ul>

        **可以作为发起方和签署方的角色列表**
        <table>
        <thead>
        <tr>
        <th>场景编号</th>
        <th>可作为发起方类型</th>
        <th>可作为签署方的类型</th>
        </tr>
        </thead>

        <tbody>
        <tr>
        <td>场景一</td>
        <td>第三方子企业A员工</td>
        <td>第三方子企业A员工</td>
        </tr>

        <tr>
        <td>场景二</td>
        <td>第三方子企业A员工</td>
        <td>第三方子企业B(不指定经办人)</td>
        </tr>

        <tr>
        <td>场景三</td>
        <td>第三方子企业A员工</td>
        <td>第三方子企业B员工</td>
        </tr>

        <tr>
        <td>场景四</td>
        <td>第三方子企业A员工</td>
        <td>个人/自然人</td>
        </tr>

        <tr>
        <td>场景五</td>
        <td>第三方子企业A员工</td>
        <td>SaaS平台企业员工</td>
        </tr>
        </tbody>
        </table>

        **注**:
        `1. 发起合同时候,  作为发起方的第三方子企业A员工的企业和员工必须经过实名, 而作为签署方的第三方子企业A员工/个人/自然人/SaaS平台企业员工/第三方子企业B员工企业中的企业和个人/员工可以未实名`

        `2. 不同类型的签署方传参不同, 可以参考开发者中心的FlowApproverInfo结构体说明`

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

        合同组是将多个合同签署流程组织在一起，多个合同同时创建，每个签署方得到一个签署链接，`一次完成合同组中多个合同的签署`。合同组的合同`不能拆分一个一个签署`，只能作为一个整体签署。

        适用场景：该接口适用于需要一次性完成多份合同签署的情况，多份合同一般具有关联性，用户以目录的形式查看合同。

        **注**:
        <ul>
        <li>此接口静默签(企业自动签)能力为白名单功能，使用前请联系对接的客户经理沟通。</li>
        <li>合同组暂不支持抄送功能</li>
        </ul>

        **可以作为发起方和签署方的角色列表**
        <table>
        <thead>
        <tr>
        <th>场景编号</th>
        <th>可作为发起方类型</th>
        <th>可作为签署方的类型</th>
        </tr>
        </thead>

        <tbody>
        <tr>
        <td>场景一</td>
        <td>第三方子企业A员工</td>
        <td>第三方子企业A员工</td>
        </tr>

        <tr>
        <td>场景二</td>
        <td>第三方子企业A员工</td>
        <td>第三方子企业B(不指定经办人)</td>
        </tr>

        <tr>
        <td>场景三</td>
        <td>第三方子企业A员工</td>
        <td>第三方子企业B员工</td>
        </tr>

        <tr>
        <td>场景四</td>
        <td>第三方子企业A员工</td>
        <td>个人/自然人</td>
        </tr>

        <tr>
        <td>场景五</td>
        <td>第三方子企业A员工</td>
        <td>SaaS平台企业员工</td>
        </tr>
        </tbody>
        </table>

        **注**:
        `1. 发起合同时候,  作为发起方的第三方子企业A员工的企业和员工必须经过实名, 而作为签署方的第三方子企业A员工/个人/自然人/SaaS平台企业员工/第三方子企业B员工企业中的企业和个人/员工可以未实名`

        `2. 不同类型的签署方传参不同, 可以参考开发者中心的FlowApproverInfo结构体说明`

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
        """指定需要批量催办的签署流程ID，批量催办合同，最多100个。需要符合以下条件的合同才可被催办
        1. 合同中当前状态为 **待签署** 的签署人是催办的对象
        2. **每个合同只能催办一次**

        **催办的效果**: 对方会受到如下的短信通知
        ![image](https://qcloudimg.tencent-cloud.cn/raw/3caf94b7f540fa5736270d38528d3a7b.png)


        **注**：`合同催办是白名单功能，请联系客户经理申请开白后使用`

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
        """该接口用于发起合同后，生成个人用户的签署链接, 暂时不支持企业端签署。 <br/>

        `注意：`<br/>
        `1. 该接口目前仅支持签署人类型是个人签署方的场景(PERSON)。` <br/>
        `2. 该接口可生成签署链接的C端签署人必须仅有手写签名和时间类型的签署控件，不支持填写控件 。` <br/>
        `3. 该签署链接有效期为30分钟，过期后将失效，如需签署可重新创建签署链接 。` <br/>
        `4. 该接口返回的签署链接适用于APP集成的场景，支持APP打开或浏览器直接打开，不支持微信小程序嵌入`。<br/>
        跳转到小程序的实现，参考微信官方文档（分为<a href="https://developers.weixin.qq.com/miniprogram/dev/api/navigate/wx.navigateToMiniProgram.html">全屏</a>、<a href="https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/openEmbeddedMiniProgram.html">半屏</a>两种方式），如何配置也可以请参考: <a href="https://qian.tencent.com/developers/company/openwxminiprogram">跳转电子签小程序配置</a>

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
        """此接口（ChannelCreateMultiFlowSignQRCode）用于创建一码多扫流程签署二维码。
        适用场景：无需填写签署人信息，可通过模板id生成签署二维码，签署人可通过扫描二维码补充签署信息进行实名签署。
        常用于提前不知道签署人的身份信息场景，例如：劳务工招工、大批量员工入职等场景。

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
        """通过此接口，可以创建企业批量签署链接，员工只需点击链接即可跳转至控制台进行批量签署。

        注：
        - 员工必须在企业下完成实名认证，且需作为批量签署合同的签署方或者领取方。
        - 仅支持传入待签署或者待领取的合同，待填写暂不支持。
        - 员工批量签署，支持多种签名方式，包括手写签名、临摹签名、系统签名、个人印章、签批控件等。

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
        """发起解除协议的主要应用场景为：基于一份已经签署的合同(签署流程)，进行解除操作。
        解除协议的模板是官方提供，经过提供法务审核，暂不支持自定义。

        注意：
        <ul><li><code>原合同必须签署完</code>成后才能发起解除协议。</li>
        <li>只有原合同企业类型的参与人才能发起解除协议，<code>个人参与方不能发起解除协议</code>。</li>
        <li>原合同个人类型参与人必须是解除协议的参与人，<code>不能更换其他第三方个人</code>参与解除协议。</li>
        <li>如果原合同企业参与人无法参与解除协议，可以指定同企业具有同等权限的<code>企业员工代为处理</code>。</li>
        <li>发起解除协议同发起其他企业合同一样，也会参与合同<code>扣费</code>，扣费标准同其他类型合同。</li>
        <li>在解除协议发起之后，原合同的状态将转变为解除中。一旦解除协议签署完毕，原合同及解除协议均变为已解除状态。</li></ul>

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
        """获取个人用户自动签的开通链接。

        注意: `处方单等特殊场景专用，此接口为白名单功能，使用前请联系对接的客户经理沟通。`

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
        """获取企业员工信息, 可以获取员工的名字,OpenId,UserId和简述的角色等信息，支持设置过滤条件以筛选员工查询结果。

        **注**:通过<a href="https://qian.tencent.com/developers/partnerApis/accounts/SyncProxyOrganizationOperators" target="_blank">企业员工新增或离职</a>接口增加的新员工或者离职的员工也会在列表中。

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
        """通过此接口获取个人用户自动签的开通状态。

        注意: `处方单等特殊场景专用，此接口为白名单功能，使用前请联系对接的客户经理沟通。`

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
        """通过此接口可以关闭个人用户自动签功能。
        无需对应的用户刷脸等方式同意即可关闭。

        注意:

        <ul><li>处方单等特殊场景专用，此接口为白名单功能，使用前请联系对接的客户经理沟通。</li>
        <li>如果此用户在开通时候绑定过个人自动签账号许可,  关闭此用户的自动签不会归还个人自动签账号许可的额度。</li></ul>

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
        """此接口（ChannelGetTaskResultApi）用来查询转换任务的状态。如需发起转换任务，请使用<a href="https://qian.tencent.com/developers/partnerApis/files/ChannelCreateConvertTaskApi" target="_blank">创建文件转换任务接口</a>进行资源文件的转换操作<br />
        前提条件：已调用 <a href="https://qian.tencent.com/developers/partnerApis/files/ChannelCreateConvertTaskApi" target="_blank">创建文件转换任务接口</a>进行文件转换，并得到了返回的转换任务Id。<br />

        适用场景：已创建一个文件转换任务，想查询该文件转换任务的状态，或获取转换后的文件资源Id。<br />
        注：
        1. `大文件转换所需的时间可能会比较长`

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
        """对合同流程文件进行数字签名验证，判断数字签名是否有效，合同文件内容是否被篡改。

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
        """提交申请出证报告任务并返回报告ID。

        注意：
        - 使用此功能**需搭配出证套餐**  ，使用前请联系对接的客户经理沟通。
        - 操作人必须是**发起方或者签署方企业的(非走授权书认证)法人或者超管**。
        - 合同流程必须**所有参与方已经签署完成**。
        - 出证过程需一定时间，建议在**提交出证任务后的24小时之后**，通过<a href="https://qian.tencent.com/developers/partnerApis/certificate/DescribeChannelFlowEvidenceReport" target="_blank">获取出证报告任务执行结果</a>接口进行查询执行结果和出证报告的下载URL。


        ![image](https://dyn.ess.tencent.cn/guide/capi/channel_CreateChannelFlowEvidenceReport.png)

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
        """此接口（CreateChannelOrganizationInfoChangeUrl）用于创建子客企业信息变更链接（需要在移动端打开，会跳转到微信小程序），支持创建企业超管变更链接或企业基础信息变更链接，通过入参 ChangeType 指定。


        <h3 id="1-企业超管变更">1. 企业超管变更</h3>

        <p>换成企业的其他员工来当超管</p>

        <h3 id="2-企业基础信息变更">2. 企业基础信息变更</h3>

        <h4 id="可以变动">可以变动</h4>

        <ul>
        <li>企业名称<br>
        </li>
        <li>法定代表人姓名(新法人有邀请链接)<br>
        </li>
        <li>企业地址和所在地</li>
        </ul>

        <h4 id="不可变动">不可变动</h4>

        <ul>
        <li>统一社会信用代码<br>
        </li>
        <li>企业主体类型</li>
        </ul>

        <p>如果企业名称变动会引起下面的变动</p>

        <ul>
        <li>合同:   老合同不做任何处理,   新发起的合同需要用新的企业名字作为签署方, 否则无法签署</li>
        <li>印章:   会删除所有的印章所有的机构公章和合同专用章,  然后用新企业名称生成新的机构公章 和合同专用章,  而法人章, 财务专用章和人事专用章不会处理</li>
        <li>证书:   企业证书会重新请求CA机构用新企业名称生成新的证书</li>
        </ul>

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
        """此接口（CreateConsoleLoginUrl）用于创建第三方平台子客企业控制台Web/移动登录链接。支持web控制台、电子签小程序和H5链接。登录链接是进入子客web企业控制台的唯一入口。

        Web链接访问后，会根据子客企业(**Agent中ProxyOrganizationOpenId表示**)和员工(**Agent中OpenId表示**)的状态，进入不同的流程，主要情况分类如下：
        <table>
        <thead>
        <tr>
        <th>子客企业状态</th>
        <th>子客企业员工状态</th>
        <th>点击链接进入的流程</th>
        </tr>
        </thead>
        <tbody>
        <tr>
        <td>企业未激活</td>
        <td>员工未认证</td>
        <td>进入企业激活流程，首次完成企业激活流程的员工会成为超管</td>
        </tr>
        <tr>
        <td>企业已激活</td>
        <td>员工未认证</td>
        <td>进入员认证并加入企业流程</td>
        </tr>
        <tr>
        <td>企业已激活</td>
        <td>员工已认证</td>
        <td>进入子客企业Web控制台</td>
        </tr>
        </tbody>
        </table>
        如果是企业激活流程，需要注意如下情况：

        1. 若在激活过程中，**更换用户OpenID重新生成链接，之前的认证会被清理**。因此不要在企业认证过程生成多个链接给多人同时操作，会导致认证过程互相影响。
        2. 若您认证中发现信息有误需要重新认证，**可通过更换用户OpenID重新生成链接的方式，来清理掉已有的流程**。

        系统的渠道企业, 应用, 子客企业, 子客员工的组织形式
        ![image](https://qcloudimg.tencent-cloud.cn/raw/bee4b7375fe7a097f3573b18a1c1e30b.png)

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

        **整体的逻辑如下**

        ![image](https://dyn.ess.tencent.cn/guide/capi/CreateFlowsByTemplates.png)

        **可以作为发起方和签署方的角色列表**
        <table>
        <thead>
        <tr>
        <th>场景编号</th>
        <th>可作为发起方类型</th>
        <th>可作为签署方的类型</th>
        </tr>
        </thead>

        <tbody>
        <tr>
        <td>场景一</td>
        <td>第三方子企业A员工</td>
        <td>第三方子企业A员工</td>
        </tr>

        <tr>
        <td>场景二</td>
        <td>第三方子企业A员工</td>
        <td>第三方子企业B(不指定经办人)</td>
        </tr>

        <tr>
        <td>场景三</td>
        <td>第三方子企业A员工</td>
        <td>第三方子企业B员工</td>
        </tr>

        <tr>
        <td>场景四</td>
        <td>第三方子企业A员工</td>
        <td>个人/自然人</td>
        </tr>

        <tr>
        <td>场景五</td>
        <td>第三方子企业A员工</td>
        <td>SaaS平台企业员工</td>
        </tr>
        </tbody>
        </table>

        **注**:
        `1. 发起合同时候,  作为发起方的第三方子企业A员工的企业和员工必须经过实名, 而作为签署方的第三方子企业A员工/个人/自然人/SaaS平台企业员工/第三方子企业B员工企业中的企业和个人/员工可以未实名`
        `2. 不同类型的签署方传参不同, 可以参考开发者中心的FlowApproverInfo结构体说明`

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
        """1. 可以**通过图片**为子客企业代创建印章，图片最大5MB

        2. 可以**系统创建**子客企业代创建印章, 系统创建的印章样子下图(样式可以调整)

        ![image](https://dyn.ess.tencent.cn/guide/capi/CreateSealByImage.png)

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
        """创建跳转小程序查看或签署的链接

        **腾讯电子签小程序的AppID 和 原始Id如下:**

        | 小程序 | AppID | 原始ID |
        | ------------ | ------------ | ------------ |
        | 腾讯电子签（正式版） | wxa023b292fd19d41d | gh_da88f6188665 |
        | 腾讯电子签Demo | wx371151823f6f3edf | gh_39a5d3de69fa |

        **主要使用场景可以更加EndPoint分类如下**

        |EndPoint| 场景| 说明和示例|
        |  ----  | ----  | --- |
        |  WEIXINAPP  | 短链跳转腾讯电子签小程序签署场景  |  点击链接打开电子签小程序（与腾讯电子签官方短信提醒用户签署形式一样）<br> 示例: https://essurl.cn/x9nvWU8fTg|
        |  LONGURL2WEIXINAPP  | 长链跳转腾讯电子签小程序签署场景  |  点击链接打开电子签小程序, 是WEIXINAPP生成短链代表的那个长链|
        |  CHANNEL  | 带有H5引导页的跳转腾讯电子签小程序签署场景 |  点击链接打开一个H5引导页面, 页面中有个"前往小程序"的按钮, 点击后会跳转到腾讯电子签小程序签署场景;  签署完成会回到H5引导页面, 然后跳转到指定创建链接指定的JumpUrl<br>示例: https://res.ess.tencent.cn/cdn/h5-activity-beta/jump-mp.html?use=channel-guide&type=warning&token=uIFKIU8fTd |
        |APP| 贵方App跳转腾讯电子签小程序签署场景|  贵方App直接跳转到小程序后, 在腾讯电子签小程序签署完成后返回贵方App的场景<br>跳转到腾讯电子签小程序的实现可以参考微信的官方文档:<a href="https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/launchApp.html" target="_blank">开放能力/打开 App</a> <br> 示例: pages/guide?from=default&where=mini& to=CONTRACT_DETAIL& id=yDwiBUUc*duRvquCSX8wd& shortKey=yDwivUA**W1yRsTre3 |
        |APP| 贵方小程序跳转腾讯电子签小程序签署场景|  贵方App直接跳转到小程序后, 在腾讯电子签小程序签署完成后返回贵方小程序的场景<br>跳转到腾讯电子签小程序的实现可以参考微信官方文档<a href="https://developers.weixin.qq.com/miniprogram/dev/api/navigate/wx.navigateToMiniProgram.html" target="_blank">全屏方式</a>和<a href="https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/openEmbeddedMiniProgram.html " target="_blank">半屏方式</a><br>此时返回的SignUrl就是官方文档中的path<br> 示例:pages/guide?from=default&where=mini& to=CONTRACT_DETAIL& id=yDwiBUUc*duRvquCSX8wd& shortKey=yDwivUA**W1yRsTre3  |

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


    def DescribeBillUsageDetail(self, request):
        """通过此接口（DescribeBillUsageDetail）查询该第三方平台子客企业的套餐消耗详情。

        :param request: Request instance for DescribeBillUsageDetail.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.DescribeBillUsageDetailRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.DescribeBillUsageDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBillUsageDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBillUsageDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeChannelFlowEvidenceReport(self, request):
        """获取出证报告任务执行结果，返回报告 URL。

        注意：

        - 使用此功能`需搭配出证套餐` ，使用前请联系对接的客户经理沟通。
        - 需调用创建并返回出证报告接口<a href="https://qian.tencent.com/developers/partnerApis/certificate/CreateChannelFlowEvidenceReport" target="_blank">提交申请出证报告任务</a>获取报告编号后调用当前接口获取报告链接。

        ![image](https://dyn.ess.tencent.cn/guide/capi/channel_CreateChannelFlowEvidenceReport.png)

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
        """查询企业扩展服务的开通和授权情况，当前支持查询以下内容：
        1. 企业自动签
        2. 企业与港澳台居民签署合同
        3. 使用手机号验证签署方身份
        4. 骑缝章
        5. 拓宽签署方年龄限制
        6. 下载企业合同/文件

        注: 此接口 参数Agent. ProxyOperator.OpenId 需要传递超管或者法人的OpenId

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
        """此接口用于查询合同或者合同组的详情信息，支持查询多个（数量不能超过100）。

        适用场景：可用于主动查询某个合同或者合同组的详情信息。

        注:  `只能查询本企业创建的合同(创建合同用的Agent和此接口用的Agent数据最好一致) `

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
        """获取合同流程PDF的下载链接，可以下载签署中、签署完的此子企业创建的合同

        **注意**:
        有两种开通权限的途径

        **第一种**:   需第三方应用的子企业登录控制台进行授权,  授权在**企业中心**的**授权管理**区域,  界面如下图
        授权过程需要**子企业超管**扫描跳转到电子签小程序签署<<渠道端下载渠道子客合同功能授权委托书>>

        ![image](https://qcloudimg.tencent-cloud.cn/raw/8b483dfebdeafac85051279406944048.png)

        **第二种**: 第三方应用的配置接口打开全第三个应用下的所有自己起开通, 需要**渠道方企业的超管**扫描二维码跳转到电子签小程序签署 <<渠道端下载渠道子客合同功能开通知情同意书>>
        ![image](https://qcloudimg.tencent-cloud.cn/raw/238979ef51dd381ccbdbc755a593debc/channel_DescribeResourceUrlsByFlows_appilications2.png)

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

        **适用场景**
         该接口常用来配合<a href="https://qian.tencent.com/developers/partnerApis/startFlows/CreateFlowsByTemplates" target="_blank">用模板创建签署流程</a>和<a href="https://qian.tencent.com/developers/partnerApis/startFlows/ChannelCreateFlowGroupByTemplates" target="_blank">通过多模板创建合同组签署流程</a>接口，作为创建合同的前置接口使用。
        通过此接口查询到模板信息后，再通过调用创建合同的接口，指定模板ID，指定模板中需要的填写控件内容等，完成合同文档的的创建。

        **模版的来源**
        子客企业的模板有两种途径获取
        - 渠道方(平台方)配置完成后, 分发给同应用的各个子企业
        - 子客企业通过CreateConsoleLoginUrl创建的链接登录子客控制台自己创建

        **一个模板通常会包含以下结构信息**

        - 模板模版ID, 模板名字等基本信息
        - 发起方参与信息Promoter、签署参与方 Recipients，后者会在模板发起合同时用于指定参与方
        - 发起方和签署方的填写控件 Components
        - 签署方的签署控件 SignComponents

        ![image](https://dyn.ess.tencent.cn/guide/capi/channel_DescribeTemplates.png)

        模版中各元素的层级关系, 所有的填写控件和签署控件都归属某一个角色(通过控件的ComponentRecipientId来关联)
        ![image](https://qcloudimg.tencent-cloud.cn/raw/45c638bd93f9c8024763add9ab47c27f.png)


        **注意**

        >1. 查询条件TemplateId、TemplateName与ChannelTemplateId可同时存在，即可查询同时满足这些条件的模板。
        >2. TemplateId 和TemplateIds互为独立，若两个参数都传入，则以TemplateId为准

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
        """此接口（GetDownloadFlowUrl）用户获取合同控制台下载页面链接,  点击链接后会跳转至本企业合同管理控制台(会筛选出传入的合同列表), 点击**下载**按钮后就会下载传入的合同列表, 下载页面如下图
        ![image](https://dyn.ess.tencent.cn/guide/capi/channel_GetDownloadFlowUrl.png)

        注:
        <ul>
        <li>仅支持下载 **本企业** 下合同，链接会 **登录企业控制台** </li>
        <li> **链接仅可使用一次**，不可重复使用</li>
        </ul>

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
        目前该接口只支持B2C，<font color='red'> **不建议使用，将会废弃**</font>。

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
        """此接口（SyncProxyOrganization）用于同步第三方平台子客企业信息，包括企业名称、企业营业执照、企业统一社会信用代码和法人姓名等，便于子客企业在企业激活过程中无需手动上传营业执照或补充企业信息。

        注意：

        - **需要在<a href="https://qian.tencent.com/developers/partnerApis/accounts/CreateConsoleLoginUrl" target="_blank">生成子客登录链接</a>前同步的企业信息**, 否则会出现信息同步没有用的情形
        - **企业信息需要和营业执照信息对应**,  否则会出现激活过程验证不通过的问题

        ![image](https://qcloudimg.tencent-cloud.cn/raw/7ec91b79a0a4860e77c9ff9f4a5f13ad/channel_SyncProxyOrganization2.png)


        - **企业统一社会信用代码**: 对应上图中的**1**
        - **第三方平台子客企业名称**: 对应上图中的**2**
        - **企业法定代表人的名字**:对应上图中的**3**
        - **企业详细住所**:对应上图中的**4**

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

        - **新增员工的场景**:    提前导入员工列表, 然后调用<a href="https://qian.tencent.com/developers/partnerApis/accounts/CreateConsoleLoginUrl" target="_blank">生成子客登录链接</a>分享给对应的员工进行实名, 新增员工后员工的状态为**未实名**, 通过链接实名后状态变为**已实名**, 已实名员工就可以参与合同的发起和签署

        - **员工离职的场景**: 将员工置为离职, 员工无法登录控制台和腾讯电子签小程序进行操作了,   同时给此员工分配的openid会被回收可以给其他新员工使用 (离职后员工数据会被置空,  再次加入公司会从零开始) ,  若员工信息有误可通过离职后在新增来解决,  离职员工状态为**离职**

        ![image](https://dyn.ess.tencent.cn/guide/capi/channel_SyncProxyOrganizationOperators.png)

        **注**:
        -  新增员工可以配置白名单限制注册使用对应openid的员工必须满足SyncProxyOrganizationOperators导入的(默认生成子客登录链接生成的链接可以任意员工点击注册绑定对应的openid), 此白名单需要咨询接入经理
        -  <font color='red'>超管和法人无法通过此接口离职</font>,  需要超管和法人将权限转移给其他人后才可通过此接口离职
        - 新增员工的场景同ID不同员工会覆盖掉上一个同ID的员工, 如果上一个员工已经实名则不会被覆盖

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
        """此接口（UploadFiles）文件上传。<br/>

        适用场景：用于合同，印章的文件上传。文件上传以后，
        如果是PDF格式文件可配合<a href="https://qian.tencent.com/developers/partnerApis/startFlows/ChannelCreateFlowByFiles" target="_blank">用PDF文件创建签署流程</a>接口进行合同流程的发起
        如果是其他类型可以配合<a href="https://qian.tencent.com/developers/partnerApis/files/ChannelCreateConvertTaskApi" target="_blank">创建文件转换任务</a>接口转换成PDF文件

        注:
        1. 图片类型(png/jpg/jpeg)限制大小为5M以下, PDF/word/excel等其他格式限制大小为60M以下
        2. <font color='red'>此接口调用时需要单独设置Domain请求域名 </font>,  联调开发环境为 **file.test.ess.tencent.cn**，正式环境需要设置为**file.ess.tencent.cn**，代码示例
        ```
        HttpProfile httpProfile = new HttpProfile();
        httpProfile.setEndpoint("file.test.ess.tencent.cn");
        ```

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