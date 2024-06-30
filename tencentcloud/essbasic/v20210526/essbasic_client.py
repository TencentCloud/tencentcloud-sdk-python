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

        批量撤销结果可以通过接口返回的TaskId关联[批量撤销任务结果回调](https://qian.tencent.com/developers/partner/callback_types_contracts_sign#%E4%B9%9D-%E6%89%B9%E9%87%8F%E6%92%A4%E9%94%80%E7%BB%93%E6%9E%9C%E5%9B%9E%E8%B0%83)或通过接口[查询批量撤销合同结果](https://qian.tencent.com/developers/partnerApis/operateFlows/DescribeCancelFlowsTask)主动查询。


        注:
        - 有对应合同撤销权限的人:  <font color='red'>**合同的发起人（并已经授予撤销权限）或者发起人所在企业的超管、法人**</font>
        - 签署完毕的合同需要双方走解除流程将合同作废，可以参考<a href="https://qian.tencent.com/developers/partnerApis/startFlows/ChannelCreateReleaseFlow" target="_blank">发起解除合同流程接口</a>
        - <font color='red'>只有撤销没有参与方签署过或只有自动签署签署过的合同，才会返还合同额度。</font>

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
        - 有对应合同撤销权限的人:  <font color='red'>**合同的发起人（并已经授予撤销权限）或者发起人所在企业的超管、法人**</font>
        - 签署完毕的合同需要双方走解除流程将合同作废，可以参考<a href="https://qian.tencent.com/developers/partnerApis/startFlows/ChannelCreateReleaseFlow" target="_blank">发起解除合同流程接口</a>
        - <font color='red'>只有撤销没有参与方签署过或只有自动签署签署过的合同，才会返还合同额度。</font>

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
        """此接口（CancelMultiFlowSignQRCode）用于废除取消一码多签签署码。
        该接口所需的二维码ID，源自[创建一码多签签署码](https://qian.tencent.com/developers/partnerApis/templates/ChannelCreateMultiFlowSignQRCode)生成的。
        如果该签署码尚处于有效期内，可通过本接口将其设置为失效状态。

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
        """通过合同编号生成批量撤销合同的链接，单次最多支持撤销100份合同,   返回的链接需要有此权限的人<font color='red'>**合同的发起人（并已经授予撤销权限）或者发起人所在企业的超管、法人**</font>在<font color='red'>**手机端**</font>打开,  跳转到腾讯电子签小程序输入撤销原因来进行撤销合同

        适用场景：如果某个合同当前**至少还有一方没有签署**，则可通过该接口取消该合同流程。常用于合同发错、内容填错，需要及时撤销的场景。

        - **可撤回合同状态**：未全部签署完成
        - **不撤回合同状态**：已全部签署完成、已拒签、已过期、已撤回、拒绝填写、已解除等合同状态。

        批量撤销结果可以通过接口返回的TaskId关联[批量撤销任务结果回调](https://qian.tencent.com/developers/partner/callback_types_contracts_sign#%E4%B9%9D-%E6%89%B9%E9%87%8F%E6%92%A4%E9%94%80%E7%BB%93%E6%9E%9C%E5%9B%9E%E8%B0%83)或通过接口[查询批量撤销合同结果](https://qian.tencent.com/developers/partnerApis/operateFlows/DescribeCancelFlowsTask)主动查询。

        注:
        - 签署完毕的合同需要双方走解除流程将合同作废，可以参考<a href="https://qian.tencent.com/developers/partnerApis/startFlows/ChannelCreateReleaseFlow" target="_blank">发起解除合同流程接口</a>
        - <font color='red'>只有撤销没有参与方签署过或只有自动签署签署过的合同，才会返还合同额度。</font>

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
        """该接口用于发起合同后，生成个人用户的批量签署链接, 暂时不支持企业端签署。
        **注意**：
        1. 该接口目前仅支持签署人类型是**个人签署方的批量签署场景**(ApproverType=PERSON)。
        2. 该接口可生成批量签署链接的C端签署人**必须仅有手写签名(控件类型为SIGN_SIGNATURE)和时间类型的签署控件**，**不支持填写控件** 。
        3. 请确保C端签署人在批量签署合同中**为待签署状态**，如需顺序签署请待前一位参与人签署完成后，再创建该C端用户的签署链接。
        4. 该签署链接**有效期为30分钟**，过期后将失效，如需签署可重新创建批量签署链接 。
        5. 该接口返回的签署链接适用于APP集成的场景，支持APP打开或浏览器直接打开，**不支持微信小程序嵌入**。
        跳转到小程序的实现，参考微信官方文档(分为<a href="https://developers.weixin.qq.com/miniprogram/dev/api/navigate/wx.navigateToMiniProgram.html">全屏</a>、<a href="https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/openEmbeddedMiniProgram.html">半屏</a>两种方式)，如何配置也可以请参考: <a href="https://qian.tencent.com/developers/company/openwxminiprogram">跳转电子签小程序配置</a>。
        6.  因h5涉及人脸身份认证能力基于慧眼人脸核身，对Android和iOS系统均有一定要求， 因此<font color='red'>App嵌入H5签署合同需要按照慧眼提供的<a href="https://cloud.tencent.com/document/product/1007/61076">慧眼人脸核身兼容性文档</a>做兼容性适配</font>。

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
        - 使用此接口生成链接，需要提前开通 `使用手机号验证签署方身份` 功能，在 `腾讯电子签网页端-企业设置-拓展服务` 中可以找到。
        - 参与人点击链接后需短信验证码才能查看合同内容。
        - 企业用户批量签署，需要传OrganizationName（参与方所在企业名称）参数生成签署链接，<font color="red">请确保此企业已完成腾讯电子签企业认证</font>。暂时仅支持给<font color="red">自建应用集成企业</font>生成员工批签链接，不支持子客企业。
        - 生成批量签署链接时，合同目标参与方状态需为<font color="red">待签署</font>状态。
        - 个人批量签署进行的合同的签名区， 全部变成<font color="red">手写签名</font>（不管合同里边设置的签名限制）来进行。

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
        """此接口（ChannelCreateBoundFlows）用于子客企业领取未归属给员工的合同，将合同领取给当前员工，合同不能重复领取。


        **未归属合同发起方式**
         指定对应企业的OrganizationOpenId和OrganizationName而不指定具体的参与人(OpenId/名字/手机号等),  则合同进入待领取状态, 示例代码如下
        ```
        		FlowApprovers: []*essbasic.FlowApproverInfo{
        			{
        				ApproverType:       common.StringPtr("ORGANIZATION"),
        				OrganizationOpenId: common.StringPtr("org_dianziqian"),
        				OrganizationName:   common.StringPtr("典子谦示例企业"),
        			}
        		},
        ```

        可以<a href="https://qian.tencent.com/developers/partnerApis/accounts/CreateConsoleLoginUrl" target="_blank">生成子客登录链接</a>登录控制台查看带领取的合同
        ![image](https://qcloudimg.tencent-cloud.cn/raw/a34d0cc56ec871613e94dfc6252bc072.png)

        注:
        1. 支持批量领取,  如果有一个合同流程无法领取会导致接口报错,  使得所有合同都领取失败
        2. 只有企业的<font color="red">超管或者法人</font>才能进行合同的领取

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

        本接口下面功能的签署页面链接的生成
        - 创建印章
        - 创建模板
        - 修改模板
        - 预览模板
        - 预览合同流程

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
        2. 个人签署人支持通过姓名+手机号进行补充，补充动态签署人时：若个人用户已完成实名，则可通过姓名+证件号码进行补充。

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

        ![image](https://qcloudimg.tencent-cloud.cn/raw/bf86248a2c163228c4e894cf5926af69/ChannelCreateFlowByFiles.png)

        **可以作为发起方和签署方的角色列表**
        <table>     <thead>     <tr>         <th>场景编号</th>         <th>发起方</th>         <th>签署方</th>         <th>补充</th>     </tr>     </thead>     <tbody>     <tr>         <td>场景一</td>         <td>子企业A的员工</td>         <td>子企业A的员工</td>         <td>子企业是通过<a href="https://qian.tencent.com/developers/partnerApis/accounts/CreateConsoleLoginUrl" target="_blank">CreateConsoleLoginUrl</a>生成子客登录链接注册的企业</td>     </tr>     <tr>         <td>场景二</td>         <td>子企业A的员工</td>         <td>子企业B(不指定经办人走领取逻辑)</td>         <td>领取的逻辑可以参考文档<a href="https://qian.tencent.com/developers/partner/dynamic_signer" target="_blank">动态签署方</a> </td>     </tr>     <tr>         <td>场景三</td>         <td>子企业A的员工</td>         <td>子企业B的员工</td>         <td>-</td>     </tr>     <tr>         <td>场景四</td>         <td>子企业A的员工</td>         <td>个人</td>         <td>就是自然人，不是企业员工</td>     </tr>     <tr>         <td>场景五</td>         <td>子企业A的员工</td>         <td>SaaS平台企业员工</td>         <td>SaaS平台企业是通过<a href="https://qian.tencent.cn/console/company-register" target="_blank">https://qian.tencent.cn/console/company-register</a>链接注册的企业</td>     </tr>     </tbody> </table>


        **注**:
        `1. 发起合同时候,  作为发起方的第三方子企业A员工的企业和员工必须经过实名, 而作为签署方的第三方子企业A员工/个人/自然人/SaaS平台企业员工/第三方子企业B员工企业中的企业和个人/员工可以未实名`

        `2. 不同类型的签署方传参不同, 可以参考开发者中心的FlowApproverInfo结构体说明`

        `3. 合同发起后就会扣减合同的额度, 只有撤销没有参与方签署过或只有自动签署签署过的合同，才会返还合同额度。（过期，拒签，签署完成，解除完成等状态不会返还额度）`

        `4. 静默（自动）签署不支持合同签署方存在填写功能`

        <font color="red">相关视频指引</font> <br>
        1. <a href="https://dyn.ess.tencent.cn/guide/apivideo/essbasic-UploadFiles.mp4" target="_blank">【上传文件代码】编写示例</a><br>
        1. <a href="https://dyn.ess.tencent.cn/guide/apivideo/essbasic-ChannelCreateFlowByFiles.mp4" target="_blank">【用PDF文件创建签署流程】编写示例</a><br>

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

        `3. 合同发起后就会扣减合同的额度, 只有撤销没有参与方签署过或只有自动签署签署过的合同，才会返还合同额度。（过期，拒签，签署完成，解除完成等状态不会返还额度），合同组中每个合同会扣减一个合同额度`

        `4. 静默（自动）签署不支持合同签署方存在填写功能`

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

        `3. 合同发起后就会扣减合同的额度, 只有撤销没有参与方签署过或只有自动签署签署过的合同，才会返还合同额度。（过期，拒签，签署完成，解除完成等状态不会返还额度），合同组中每个合同会扣减一个合同额度`

        `4. 静默（自动）签署不支持合同签署方存在填写功能`

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

        **催办的效果**: 对方会收到如下的短信通知

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
        **当前存在两种审核操作：**
        <ul>
        <li>签署审核
        <ul>
        <li>在通过接口<ul><li>CreateFlowsByTemplates</li><li>ChannelCreateFlowByFiles</li><li>ChannelCreateFlowGroupByTemplates</li><li>ChannelCreateFlowGroupByFiles</li><li>ChannelCreatePrepareFlow</li></ul> 发起签署流程时，通过指定NeedSignReview为true，则可以调用此接口，并指定operate=SignReview，以提交企业内部签署审批结果</li>
        <li>在通过接口<ul><li>CreateFlowsByTemplates</li><li>ChannelCreateFlowByFiles</li><li>ChannelCreateFlowGroupByTemplates</li><li>ChannelCreateFlowGroupByFiles</li></ul>发起签署流程时，通过指定签署人ApproverNeedSignReview为true，则可以调用此接口，并指定operate=SignReview，并指定RecipientId，以提交企业内部签署审批结果</li>
        </ul>
        </li>
        <li>发起审核
         <ul>
        <li>通过接口ChannelCreatePrepareFlow指定发起后需要审核，那么可以调用此接口，并指定operate=CreateReview，以提交企业内部审批结果。可以多次提交审批结果，但一旦审批通过，后续提交的结果将无效
        </li>
        </ul>
        </li>
        </ul>

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
        """该接口用于发起合同后，生成用户的签署链接 <br/>

        **注意**
        1. 该签署**链接有效期为30分钟**，过期后将失效，如需签署可重新创建签署链接 。
        2. 该接口返回的签署链接适用于APP集成的场景，支持APP打开或浏览器直接打开，**不支持微信小程序嵌入**。配置方式请参考：<a href="https://qian.tencent.com/developers/company/openqianh5/">跳转电子签H5</a>。
        如需跳转到小程序的实现，参考微信官方文档（分为<a href="https://developers.weixin.qq.com/miniprogram/dev/api/navigate/wx.navigateToMiniProgram.html">全屏</a>、<a href="https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/openEmbeddedMiniProgram.html">半屏</a>两种方式），如何配置也可以请参考: <a href="https://qian.tencent.com/developers/company/openwxminiprogram">跳转电子签小程序配置</a>。
        3. 因h5涉及人脸身份认证能力基于慧眼人脸核身，对Android和iOS系统均有一定要求， 因此<font color='red'>App嵌入H5签署合同需要按照慧眼提供的<a href="https://cloud.tencent.com/document/product/1007/61076">慧眼人脸核身兼容性文档</a>做兼容性适配</font>。

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
        """此接口（ChannelCreateMultiFlowSignQRCode）用于创建一码多签签署码。

        **适用场景**:
        签署人可通过扫描二维码补充签署信息进行实名签署。常用于提前不知道签署人的身份信息场景，例如：劳务工招工、大批量员工入职等场景。

        **注意**:
        1. 本接口适用于**发起方没有填写控件的 B2C或者单C模板**,  若是B2C模板,还要满足以下任意一个条件
            - 模板中配置的签署顺序是无序
            - B端企业的签署方式是静默签署
            - B端企业是非首位签署
        2. 通过扫描一码多签签署码发起的合同，合同涉及到的回调消息可参考文档[合同发起及签署相关回调
        ]( https://qian.tencent.com/developers/partner/callback_types_contracts_sign)
        3. 用户通过扫描一码多签签署码发起合同时，因企业额度不足导致失败 会触发签署二维码相关回调,具体参考文档[签署二维码相关回调](https://qian.tencent.com/developers/partner/callback_types_commons#%E7%AD%BE%E7%BD%B2%E4%BA%8C%E7%BB%B4%E7%A0%81%E7%9B%B8%E5%85%B3%E5%9B%9E%E8%B0%83)

        签署码的样式如下图:
        ![image](https://qcloudimg.tencent-cloud.cn/raw/27317cf5aacb094fb1dc6f94179a5148.png )

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
        """通过此接口指定合同、签署人、填写控件等信息，生成嵌入式链接，此链接可以嵌入到其他网页或者直接打开，打开后进入发起页面。在此页面上，合同信息和签署人信息均不可更改。

        注意：
        1. <font color="red">仅支持在PC浏览器</font>上进行操作和使用。
        2. 在使用<font color="red">模板发起合同时，需指定RecipientId</font>以明确参与方在模板中所扮演的角色。

        **嵌入式签署人-各种场景传参说明**:

        <table>
        <thead>
        <tr>
        <th>场景编号</th>
        <th>可作为签署方的类型</th>
        <th>签署方传参说明</th>
        </tr>
        </thead>

        <tbody>
        <tr>
        <td>场景一</td>
        <td>第三方子企业员工</td>
        <td>OpenId、OrganizationName、OrganizationOpenId必传 ,ApproverType设置为0</td>
        </tr>
        <tr>
        <td>场景二</td>
        <td>SaaS平台企业员工</td>
        <td>Name、Mobile、OrganizationName必传，NotChannelOrganization=True。 ApproverType设置为0</td>
        </tr>
        <tr>
        <td>场景三</td>
        <td>个人/自然人</td>
        <td>Name、Mobile必传, ApproverType设置为1</td>
        </tr>
        </tbody>
        </table>

        嵌入的页面样式如下：
        ![image](https://qcloudimg.tencent-cloud.cn/raw/b2ae013fb4d747891dd3815bbe897208.png)

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
        <li>在解除协议签署完毕后，原合同及解除协议均变为已解除状态。</li>
        <li>非原合同企业参与人发起解除协议时，需要有<code>解除合同的权限</code>。</li>
        </ul>

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

        适用场景2：创建当前企业的自定义角色，并且创建时进行权限的设置（PermissionGroups 参数要传），权限树内容 PermissionGroups 可参考[查询角色列表接口](https://qian.tencent.com/developers/partnerApis/accounts/ChannelDescribeRoles) 的输出。此处注意权限树内容可能会更新，需尽量拉取最新的权限树内容，并且权限树内容 PermissionGroups 必须是一颗完整的权限树。

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
        """使用此接口，用来绑定企业实名员工的角色，
        支持以电子签userId、客户系统openId两种方式进行绑定。

        对应控制台的操作如下图
        ![image](https://qcloudimg.tencent-cloud.cn/raw/5b41194d3cb3f2058ec0ba0fb5ebc6a6.png)

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

        对应控制台的操作如下图
        ![image](https://qcloudimg.tencent-cloud.cn/raw/5b41194d3cb3f2058ec0ba0fb5ebc6a6.png)

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
        """此接口（ChannelDeleteSealPolicies）用于删除已指定员工印章授权信息，删除员工的印章授权后，该员工使用印章进行盖章时，将需要提交印章授权申请且通过审核后才能使用该印章进行签署。

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


    def ChannelDescribeBillUsageDetail(self, request):
        """通过此接口（ChannelDescribeBillUsageDetail）查询该第三方平台子客企业的套餐消耗详情。可以支持单个子客和整个应用下所有子客的查询。
        <ul>
        <li>对于单个子客企业的查询，通过指定子客的唯一标识(Agent.ProxyOrganizationOpenId)来查询该子客消耗详情</li>
        <li>对于整个应用下所有企业的查询，不需要指定子客的唯一标识，只需要传入渠道应用标识(Agent.AppId)直接查询整个应用下所有子客企业消耗详情</li>
        </ul>

        :param request: Request instance for ChannelDescribeBillUsageDetail.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.ChannelDescribeBillUsageDetailRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.ChannelDescribeBillUsageDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ChannelDescribeBillUsageDetail", params, headers=headers)
            response = json.loads(body)
            model = models.ChannelDescribeBillUsageDetailResponse()
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
        """用于获取合同中填写控件填写状态和填写的内容。

        **注意**: `附件控件不会出现在结果列表中`


        **授权**:
        此接口需要授权,  有两种开通权限的途径

        **第一种**:   需第三方应用的子企业登录控制台进行授权,  授权在**企业中心**的**授权管理**区域,  界面如下图
        授权过程需要**子企业超管**扫描跳转到电子签小程序签署<<渠道端下载渠道子客合同功能授权委托书>>

        ![image](https://qcloudimg.tencent-cloud.cn/raw/8b483dfebdeafac85051279406944048.png)

        **第二种**: 第三方应用的配置接口打开全第三个应用下的所有自己起开通, 需要**渠道方企业的超管**扫描二维码跳转到电子签小程序签署 <<渠道端下载渠道子客合同功能开通知情同意书>>
        ![image](https://qcloudimg.tencent-cloud.cn/raw/238979ef51dd381ccbdbc755a593debc/channel_DescribeResourceUrlsByFlows_appilications2.png)

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
        """此接口查询子企业电子印章。<br />

        注：
        1. 此操作要求操作者具备<b>印章查询权限</b>（若调用者尚无此权限，请联系超级管理员前往Web控制台【组织管理】->【角色管理】添加相应权限）。

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


        <font color="red">系统默认角色</font>说明可参考下表

        | 角色名称| 建议授予对象 | 角色描述 |
        | --- | --- | --- |
        | **超级管理员** |电子签业务最高权限，可以授权给法务/企业法人/业务负责人等 | 所有功能和数据管理权限，只能设置一位超管。 |
        | **业务管理员**|IT 系统负责人，可以授权给CTO等 | 企业合同模块、印章模块、模板模块等全量功能及数据权限。 |
        | **经办人**|企业法务负责人等 | 发起合同、签署合同（含填写、拒签）、撤销合同、持有印章等权限能力，可查看企业所有合同数据。 |
        | **业务员**|销售员、采购员 等| 发起合同、签署合同（含填写、拒签）、撤销合同、持有印章等权限能力，可查看自己相关所有合同数据。 |

        附件：<a href="https://dyn.ess.tencent.cn/guide/apivideo/roles.xlsx" target="_blank">点击下载角色对应的权限点的excel文档</a>

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


    def ChannelDescribeSignFaceVideo(self, request):
        """该接口用于在使用视频认证方式签署合同后，获取用户的签署人脸认证视频。

        1. 该接口**仅适用于在H5端签署**的合同，**在通过视频认证后**获取人脸图片。
        2. 该接口**不支持小程序端**的签署人脸图片获取。
        3. 请在**签署完成后的三天内**获取人脸图片，**过期后将无法获取**。

        **注意：该接口需要开通白名单，请联系客户经理开通后使用。**

        :param request: Request instance for ChannelDescribeSignFaceVideo.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.ChannelDescribeSignFaceVideoRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.ChannelDescribeSignFaceVideoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ChannelDescribeSignFaceVideo", params, headers=headers)
            response = json.loads(body)
            model = models.ChannelDescribeSignFaceVideoResponse()
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

        适用场景2：更新当前企业的自定义角色的权限信息，更新时进行权限的设置（PermissionGroups 参数要传），权限树内容 PermissionGroups 可参考[查询角色列表接口](https://qian.tencent.com/developers/partnerApis/accounts/ChannelDescribeRoles) 的输出。此处注意权限树内容可能会更新，需尽量拉取最新的权限树内容，并且权限树内容 PermissionGroups 必须是一颗完整的权限树。

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


    def ChannelRenewAutoSignLicense(self, request):
        """给医疗个人自动签许可续期。续期成功后，可对医疗自动签许可追加一年有效期，只可续期一次。

        注意: `处方单等特殊场景专用，此接口为白名单功能，使用前请联系对接的客户经理沟通。`

        :param request: Request instance for ChannelRenewAutoSignLicense.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.ChannelRenewAutoSignLicenseRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.ChannelRenewAutoSignLicenseResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ChannelRenewAutoSignLicense", params, headers=headers)
            response = json.loads(body)
            model = models.ChannelRenewAutoSignLicenseResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ChannelUpdateSealStatus(self, request):
        """此接口（ChannelUpdateSealStatus）用于第三方应用平台为子客企业更新印章状态。

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


    def CreateBatchOrganizationRegistrationTasks(self, request):
        """本接口（CreateBatchOrganizationRegistrationTasks）用于批量创建企业认证链接
        该接口为异步提交任务接口,需要跟查询企业批量认证链接(DescribeBatchOrganizationRegistrationUrls) 配合使用.

        批量创建链接有以下限制：
        1. 单次最多创建10个子客。
        2. 一天同一家企业最多创建8000个子客。
        3. 同一批创建的子客不能重复 其中包括 企业名称，企业统一信用代码，子客经办人openId。
        4. 跳转到小程序的实现，参考微信官方文档（分为全屏、半屏两种方式），如何配置也可以请参考: 跳转电子签小程序配置

        注： 1. 如果生成的链接是APP链接，跳转到小程序的实现，参考微信官方文档（分为<a href="https://developers.weixin.qq.com/miniprogram/dev/api/navigate/wx.navigateToMiniProgram.html">全屏</a>、<a href="https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/openEmbeddedMiniProgram.html">半屏</a>两种方式），如何配置也可以请参考: <a href="https://qian.tencent.com/developers/company/openwxminiprogram">跳转电子签小程序配置</a>

        **腾讯电子签小程序的AppID 和 原始Id如下:**

        | 小程序 | AppID | 原始ID |
        | ------------ | ------------ | ------------ |
        | 腾讯电子签（正式版） | wxa023b292fd19d41d | gh_da88f6188665 |
        | 腾讯电子签Demo | wx371151823f6f3edf | gh_39a5d3de69fa |

        :param request: Request instance for CreateBatchOrganizationRegistrationTasks.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.CreateBatchOrganizationRegistrationTasksRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.CreateBatchOrganizationRegistrationTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateBatchOrganizationRegistrationTasks", params, headers=headers)
            response = json.loads(body)
            model = models.CreateBatchOrganizationRegistrationTasksResponse()
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


        ![image](https://qcloudimg.tencent-cloud.cn/raw/1b4307ed143a992940c41d61192d3a0f/channel_CreateChannelFlowEvidenceReport.png)

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
        """此接口（CreateChannelOrganizationInfoChangeUrl）用于创建子客企业信息变更链接。

        <h3 id="1">支持变更链接类型，通过入参 Endpoint 指定，默认为WEIXINAPP。</h3>

        <h4 id="WEIXINAPP">WEIXINAPP</h4>
        <p>创建变更短链。需要在移动端打开，会跳转到微信腾讯电子签小程序进行更换。</p>

        <h4 id="APP">APP</h4>
        <p>创建变更小程序链接，可从第三方App跳转到微信腾讯电子签小程序进行更换。</p>


        <h3 id="2">支持创建企业超管变更链接或企业基础信息变更链接，通过入参 ChangeType 指定。</h3>

        <h4 id="1-企业超管变更">1. 企业超管变更</h4>

        <p>换成企业的其他员工来当超管</p>

        <h4 id="2-企业基础信息变更">2. 企业基础信息变更</h4>

        <h5 id="可以变动">可以变动</h5>

        <ul>
        <li>企业名称<br>
        </li>
        <li>法定代表人姓名(新法人有邀请链接)<br>
        </li>
        <li>企业地址和所在地</li>
        </ul>

        <h5 id="不可变动">不可变动</h5>

        <ul>
        <li>统一社会信用代码<br>
        </li>
        <li>企业主体类型</li>
        </ul>

        <p>如果企业名称变动会引起下面的变动</p>

        <ul>
        <li>合同:   老合同不做任何处理,   新发起的合同需要用新的企业名字作为签署方, 否则无法签署</li>
        <li>印章:   会删除所有的印章所有的机构公章，合同专用章，财务专用章和人事专用章,  然后用新企业名称生成新的机构公章，合同专用章，财务专用章和人事专用章,  而法人章不会处理</li>
        <li>证书:   企业证书会重新请求CA机构用新企业名称生成新的证书</li>
        </ul>


        注意：
        1. 生成的电子签小程序链接<font color='red'>只能由企业的法人或者超管</font>点击后进行操作， 其他员工打开后会提示“无权查看该内容”
        2. 法人可以无需生成链接，直接在电子签小程序中更换本企业的超管

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


        <font color="red">相关视频指引</font> <br>
        1. <a href="https://dyn.ess.tencent.cn/guide/apivideo/essbasic-createconsoleloginin.mp4" target="_blank">【生成子客登录链接】代码编写 &  子企业认证示例</a><br>

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


    def CreateFlowBlockchainEvidenceUrl(self, request):
        """获取区块链存证证书查看链接/二维码接口

        适用场景：企业员工可以通过此接口生成合同区块链存证证书的查看链接/二维码，以供他人扫码打开腾讯电子签小程序查看。

        [点击查看区块链存证证书样式](https://qcloudimg.tencent-cloud.cn/raw/47d5e9c2ffa90ad4e27b3cd14095aa08.jpg)

        注：
        <ul><li>1. 二维码下载链接过期时间为5分钟，请尽快下载保存。二维码/短链的过期时间为<font color="red">7天</font>，超过有效期则不可用。</li>
        <li>2. 合同状态需为<font color="red">签署完成</font> 、<font color="red">已解除</font>才能生成证书查看二维码/短链。</li>
        <li>3. 调用接口时，需确保接口调用身份拥有此合同的访问数据权限或为合同参与方。</li>
        <li>4. 通过扫码或者点击链接，用户无需登录或者鉴权即可查看对应合同的区块链存证证书，请妥善保管好二维码或链接。</li></ul>

        :param request: Request instance for CreateFlowBlockchainEvidenceUrl.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.CreateFlowBlockchainEvidenceUrlRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.CreateFlowBlockchainEvidenceUrlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateFlowBlockchainEvidenceUrl", params, headers=headers)
            response = json.loads(body)
            model = models.CreateFlowBlockchainEvidenceUrlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateFlowGroupSignReview(self, request):
        """1. 在使用[通过多文件创建合同组签署流程](https://qian.tencent.com/developers/partnerApis/startFlows/ChannelCreateFlowGroupByFiles)或[通过多模板创建合同组签署流程](https://qian.tencent.com/developers/partnerApis/startFlows/ChannelCreateFlowGroupByTemplates)创建合同组签署流程时，若指定了参数以下参数为true,则可以调用此接口提交企业内部签署审批结果,即使是自动签署也需要进行审核通过才会进行签署。
          - [FlowInfo.NeedSignReview](https://qian.tencent.com/developers/partnerApis/dataTypes/#flowinfo)
          - [FlowFileInfo.NeedSignReview](https://qian.tencent.com/developers/partnerApis/dataTypes/#flowfileinfo)
          - [FlowApproverInfo.ApproverNeedSignReview](https://qian.tencent.com/developers/partnerApis/dataTypes/#flowapproverinfo)

        2. 同一合同组，同一签署人可以多次提交签署审批结果，签署时的最后一个“审批结果”有效。

        :param request: Request instance for CreateFlowGroupSignReview.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.CreateFlowGroupSignReviewRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.CreateFlowGroupSignReviewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateFlowGroupSignReview", params, headers=headers)
            response = json.loads(body)
            model = models.CreateFlowGroupSignReviewResponse()
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

        ### 一. 整体的逻辑如下

        ![image](https://qcloudimg.tencent-cloud.cn/raw/e193519d4383fa74782a9e19147ef01a/CreateFlowsByTemplates.png)

        ###  二. 可以作为发起方和签署方的角色列表

        <table>     <thead>     <tr>         <th>场景编号</th>         <th>发起方</th>         <th>签署方</th>         <th>补充</th>     </tr>     </thead>     <tbody>     <tr>         <td>场景一</td>         <td>子企业A的员工</td>         <td>子企业A的员工</td>         <td>子企业是通过<a href="https://qian.tencent.com/developers/partnerApis/accounts/CreateConsoleLoginUrl" target="_blank">CreateConsoleLoginUrl</a>生成子客登录链接注册的企业</td>     </tr>     <tr>         <td>场景二</td>         <td>子企业A的员工</td>         <td>子企业B(不指定经办人走领取逻辑)</td>         <td>领取的逻辑可以参考文档<a href="https://qian.tencent.com/developers/partner/dynamic_signer" target="_blank">动态签署方</a> </td>     </tr>     <tr>         <td>场景三</td>         <td>子企业A的员工</td>         <td>子企业B的员工</td>         <td>-</td>     </tr>     <tr>         <td>场景四</td>         <td>子企业A的员工</td>         <td>个人</td>         <td>就是自然人，不是企业员工</td>     </tr>     <tr>         <td>场景五</td>         <td>子企业A的员工</td>         <td>SaaS平台企业员工</td>         <td>SaaS平台企业是通过<a href="https://qian.tencent.cn/console/company-register" target="_blank">https://qian.tencent.cn/console/company-register</a>链接注册的企业</td>     </tr>     </tbody> </table>




        ### 三. 填充模板中定义的填写控件
        模板中配置的<font color="red">发起人填充控件</font>可以通过本接口的**FormFields数组**字段填充

        ![image](https://qcloudimg.tencent-cloud.cn/raw/37457e0e450fc221effddfcb8b1bad55.png)
        填充的传参示例如下

        ```
            request.FormFields = [{
                    "ComponentName": "项目的名字",
                    "ComponentValue": "休闲山庄"
                }, {
                    "ComponentName": "项目的地址",
                    "ComponentValue": "凤凰山北侧",
                }, {
                    "ComponentName": "范围",
                    "ComponentValue": "凤凰山至107国道",
                }, {
                    "ComponentName": "面积",
                    "ComponentValue": "100亩",
                }, {
                    "ComponentName": "基本情况",
                    "ComponentValue": "完好",
                }, , {
                    "ComponentName": "用途",
                    "ComponentValue": "经营农家乐",
                }
            ]
        ```
        合成后合同样子示例

        ![image](https://qcloudimg.tencent-cloud.cn/raw/140a2fb771ac66a185d0a000d37485f6.png)



        ### 四. 注意
        1. 发起合同时候,  作为<font color="red">发起方的第三方子企业A员工的企业和员工必须经过实名</font>, 而作为签署方的第三方子企业A员工/个人/自然人/SaaS平台企业员工/第三方子企业B员工企业中的企业和个人/员工可以未实名

        2. 不同类型的签署方传参不同, 可以参考开发者中心的FlowApproverInfo结构体说明

        3. <font color="red">调用接口发起合同成功就会扣减合同的额度</font>, 只有撤销没有参与方签署过或只有自动签署签署过的合同，才会返还合同额度。（过期，拒签，签署完成，解除完成等状态不会返还额度）

        4. <font color="red">静默（自动）签署不支持合同签署方存在填写</font>

        5.  <font color="red">在下一步创建签署链接前，建议等待DocumentFill </font> <a href="https://qian.tencent.com/developers/partner/callback_types_file_resources">PDF合成完成的回调</a>或者睡眠几秒，尤其是当模板中存在动态表格等复杂填写控件时，因为合成过程可能会耗费秒级别的时间。


        <font color="red">相关视频指引</font> <br>
        1. <a href="https://dyn.ess.tencent.cn/guide/apivideo/essbasic-CreateTemplates.mp4" target="_blank">创建模板&设置成本企业自动签署</a><br>
        2. <a href="https://dyn.ess.tencent.cn/guide/apivideo/essbasic-CreateFlowsByTemplates.mp4" target="_blank">【用模板创建签署流程】编写示例视频教程</a><br>

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


    def CreateLegalSealQrCode(self, request):
        """该接口用于获取创建法人章的二维码，需要通过微信扫描。扫描后将跳转到腾讯电子签署，进入到创建法人章的流程。

        **注意**
        1. 该二维码**有效期为7天**，过期后将失效，可重新创建 。
        2. 每个公司**只能有1个法人章**，无法重复创建或者创建多个

        法人章的样式可以参考下图索引（也可以自己上传法人印章图片）：

        ![image](https://qcloudimg.tencent-cloud.cn/raw/36a0a090750c45bb5cac5047ac461b2c.png)

        :param request: Request instance for CreateLegalSealQrCode.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.CreateLegalSealQrCodeRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.CreateLegalSealQrCodeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateLegalSealQrCode", params, headers=headers)
            response = json.loads(body)
            model = models.CreateLegalSealQrCodeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreatePartnerAutoSignAuthUrl(self, request):
        """创建他方自动签授权链接，通过该链接可进入小程序进行合作方企业的自动签授权，若当前企业未开通企业自动签，通过该链接会先引导开通本企业自动签。
        该接口效果同控制台： 企业设置-> 扩展服务 -> 企业自动签署 -> 合作企业方授权



        注:
        1. <font color='red'>所在企业的超管、法人才有权限调用此接口</font>(Agent.ProxyOperator.OpenId 需要传递超管或者法人的OpenId)
        2. 已经在授权中或者授权成功的企业，无法重复授权

        :param request: Request instance for CreatePartnerAutoSignAuthUrl.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.CreatePartnerAutoSignAuthUrlRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.CreatePartnerAutoSignAuthUrlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreatePartnerAutoSignAuthUrl", params, headers=headers)
            response = json.loads(body)
            model = models.CreatePartnerAutoSignAuthUrlResponse()
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

        **主要使用场景EndPoint分类**

        |EndPoint| 场景| 说明和示例|
        |  ----  | ----  | --- |
        |  WEIXINAPP  | 短链跳转腾讯电子签小程序签署场景  |  点击链接打开电子签小程序（与腾讯电子签官方短信提醒用户签署形式一样）<br> 示例: https://essurl.cn/x9nvWU8fTg|
        |  LONGURL2WEIXINAPP  | 长链跳转腾讯电子签小程序签署场景  |  点击链接打开电子签小程序, 是WEIXINAPP生成短链代表的那个长链|
        |  CHANNEL  | 带有H5引导页的跳转腾讯电子签小程序签署场景 |  点击链接打开一个H5引导页面, 页面中有个"前往小程序"的按钮, 点击后会跳转到腾讯电子签小程序签署场景;  签署完成会回到H5引导页面, 然后跳转到指定创建链接指定的JumpUrl<br>示例: https://res.ess.tencent.cn/cdn/h5-activity-beta/jump-mp.html?use=channel-guide&type=warning&token=uIFKIU8fTd |
        |APP| <font color="red">贵方APP</font>跳转腾讯电子签小程序签署场景|  贵方App直接跳转到小程序后, 在腾讯电子签小程序签署完成后返回贵方App的场景<br>跳转到腾讯电子签小程序的实现可以参考微信的官方文档:<a href="https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/launchApp.html" target="_blank">开放能力/打开 App</a> <br> 示例: pages/guide?from=default&where=mini& to=CONTRACT_DETAIL& id=yDwiBUUc*duRvquCSX8wd& shortKey=yDwivUA**W1yRsTre3 |
        |APP| <font color="red">贵方小程序</font>跳转腾讯电子签小程序签署场景|  贵方小程序直接跳转到小程序后, 在腾讯电子签小程序签署完成后返回贵方小程序的场景<br>跳转到腾讯电子签小程序的实现可以参考微信官方文档<a href="https://developers.weixin.qq.com/miniprogram/dev/api/navigate/wx.navigateToMiniProgram.html" target="_blank">全屏方式</a>和<a href="https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/openEmbeddedMiniProgram.html " target="_blank">半屏方式</a><br>此时返回的SignUrl就是官方文档中的path<br> 示例:pages/guide?from=default&where=mini& to=CONTRACT_DETAIL& id=yDwiBUUc*duRvquCSX8wd& shortKey=yDwivUA**W1yRsTre3  |

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


    def DescribeBatchOrganizationRegistrationUrls(self, request):
        """此接口用于获取企业批量认证异步任务的状态及结果。

        前提条件：已调用 CreateBatchOrganizationRegistrationTasks创建企业批量认证链接任务接口，并得到了任务Id。

        异步任务的处理完成时间视当前已提交的任务量、任务的复杂程度等因素决定，正常情况下 3~5 秒即可完成，但也可能需要更长的时间

        :param request: Request instance for DescribeBatchOrganizationRegistrationUrls.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.DescribeBatchOrganizationRegistrationUrlsRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.DescribeBatchOrganizationRegistrationUrlsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBatchOrganizationRegistrationUrls", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBatchOrganizationRegistrationUrlsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCancelFlowsTask(self, request):
        """通过接口[批量撤销合同流程](https://qian.tencent.com/developers/partnerApis/operateFlows/ChannelBatchCancelFlows)或者[获取批量撤销签署流程腾讯电子签小程序链接](https://qian.tencent.com/developers/partnerApis/operateFlows/ChannelCreateBatchCancelFlowUrl)发起批量撤销任务后，可通过此接口查询批量撤销任务的结果。

        :param request: Request instance for DescribeCancelFlowsTask.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.DescribeCancelFlowsTaskRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.DescribeCancelFlowsTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCancelFlowsTask", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCancelFlowsTaskResponse()
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

        ![image](https://qcloudimg.tencent-cloud.cn/raw/1b4307ed143a992940c41d61192d3a0f/channel_CreateChannelFlowEvidenceReport.png)

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


    def DescribeChannelOrganizations(self, request):
        """查询渠道子客企业信息时，可以支持单个子客和整个应用下所有子客的查询。返回的信息包括超管、法人的信息以及当前企业的认证状态等信息。

        - 对于单个企业的查询，通过**指定子客的唯一标识**来查询该子客的企业信息
        - 对于整个应用下所有企业的查询，**不需要指定子客的唯一标识**，直接查询整个应用下所有子客企业的企业信息

        :param request: Request instance for DescribeChannelOrganizations.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.DescribeChannelOrganizationsRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.DescribeChannelOrganizationsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeChannelOrganizations", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeChannelOrganizationsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeChannelSealPolicyWorkflowUrl(self, request):
        """生成用印申请审批链接，审批人可以通过此链接进入小程序进行审批。
         p.s.
        Agent参数中的OpenId 必须为审批者的openId，且链接必须由审批人打开。

        :param request: Request instance for DescribeChannelSealPolicyWorkflowUrl.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.DescribeChannelSealPolicyWorkflowUrlRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.DescribeChannelSealPolicyWorkflowUrlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeChannelSealPolicyWorkflowUrl", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeChannelSealPolicyWorkflowUrlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeExtendedServiceAuthDetail(self, request):
        """查询企业扩展服务的授权详情（列表），当前支持查询以下内容：

        1. **企业自动签**
        2. **批量签署**


        注: <font color='red'>所在企业的超管、法人才有权限调用此接口</font>(Agent.ProxyOperator.OpenId 需要传递超管或者法人的OpenId)

        :param request: Request instance for DescribeExtendedServiceAuthDetail.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.DescribeExtendedServiceAuthDetailRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.DescribeExtendedServiceAuthDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeExtendedServiceAuthDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeExtendedServiceAuthDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeExtendedServiceAuthInfo(self, request):
        """查询企业扩展服务的开通和授权情况，当前支持查询以下内容：

        1. **企业自动签**
        2. **企业与港澳台居民签署合同**
        3. **使用手机号验证签署方身份**
        4. **骑缝章**
        5. **拓宽签署方年龄限制**
        6. **下载企业合同/文件**
        7. **隐藏合同经办人姓名**

        对应能力开通页面在子客控制台-企业中心-拓展服务，如下图所示:

        ![image](https://qcloudimg.tencent-cloud.cn/raw/931a1e02955ab36e5cc69a489af10352.jpg)

        注: <font color='red'>所在企业的超管、法人才有权限调用此接口</font>(Agent.ProxyOperator.OpenId 需要传递超管或者法人的OpenId)

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

        **第一种**:   需第三方应用的子企业登录控制台进行授权,  授权在**企业中心**的**授权管理**区域,  界面如下图。
        授权过程需要**子企业超管**扫描跳转到电子签小程序签署<<渠道端下载渠道子客合同功能授权委托书>>

        ![image](https://qcloudimg.tencent-cloud.cn/raw/8b483dfebdeafac85051279406944048.png)

        **第二种**: 渠道方企业在**企业应用管理**的配置界面打开需要配置的应用，点击**应用扩展服务**开通此功能，需要**渠道方企业的超管**扫描二维码跳转到电子签小程序签署 <<渠道端下载渠道子客合同功能开通知情同意书>>
        注:
        1. `请注意如果第三方应用的子客主动关闭了渠道端下载渠道子客合同功能开关，那么渠道方开通了此功能也无法下载子客的合同文件`
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
        通过此接口查询到模板信息后，再通过调用创建合同的接口，指定模板ID，指定模板中需要的填写控件内容等，完成合同文档的创建。

        **模板的来源**
        子客企业的模板有两种途径获取
        - 渠道方(平台方)配置完成后, 分发给同应用的各个子企业
        - 子客企业通过CreateConsoleLoginUrl创建的链接登录子客控制台自己创建

        **一个模板通常会包含以下结构信息**

        - 模板ID, 模板名字等基本信息
        - 发起方参与信息Promoter、签署参与方 Recipients，后者会在模板发起合同时用于指定参与方
        - 发起方和签署方的填写控件 Components
        - 签署方的签署控件 SignComponents

        ![image](https://qcloudimg.tencent-cloud.cn/raw/ab81fa948a0a6fea14f48cac91d0e36a/channel_DescribeTemplates.png)

        模板中各元素的层级关系, 所有的填写控件和签署控件都归属某一个角色(通过控件的ComponentRecipientId来关联)

        ![image](https://qcloudimg.tencent-cloud.cn/raw/45c638bd93f9c8024763add9ab47c27f.png)


        **注意**

        >1. 查询条件TemplateId、TemplateName与ChannelTemplateId可同时存在，即可查询同时满足这些条件的模板。
        >2. TemplateId 和TemplateIds互为独立，若两个参数都传入，则以TemplateId为准

        <font color="red">相关视频指引</font> <br>
        1. <a href="https://dyn.ess.tencent.cn/guide/apivideo/essbasic-CreateTemplates.mp4" target="_blank">创建模板&设置成本企业自动签署</a><br>

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
        """此接口（DescribeUsage）用于获取此应用下子客企业的合同消耗数量。

        注: 此接口**每日限频50次**，若要扩大限制次数,请提前与客服经理或邮件至e-contract@tencent.com进行联系。

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
        <li>仅支持下载 <b>本企业</b> 下合同，链接会 <b>登录企业控制台</b> </li>
        <li> <b>链接仅可使用一次</b>，不可重复使用</li>
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
        """管理企业扩展服务 ，企业经办人需要是企业超管或者法人。

        跳转小程序的几种方式：主要是设置不同的EndPoint
        1. 通过链接Url直接跳转到小程序，不需要返回
        设置EndPoint为WEIXINAPP，得到链接打开即可。

        2. 客户App直接跳转到小程序-->腾讯电子签小程序操作完成-->返回App
        跳转到小程序的实现，参考官方文档<a href="https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/launchApp.html">打开 App</a>
        设置EndPoint为APP，得到path。

        3. 客户小程序直接跳到电子签小程序-->腾讯电子签小程序操作完成--->回到客户小程序
        跳转到小程序的实现，参考官方文档（分为<a href="https://developers.weixin.qq.com/miniprogram/dev/api/navigate/wx.navigateToMiniProgram.html">全屏</a>、<a href="https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/openEmbeddedMiniProgram.html">半屏</a>两种方式），如何配置也可以请参考: <a href="https://qian.tencent.com/developers/company/openwxminiprogram">跳转电子签小程序配置</a>
        设置EndPoint为APP，得到path。

        4.其中小程序的原始Id如下，或者查看小程序信息自助获取。

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


    def ModifyFlowDeadline(self, request):
        """在已发起的签署流程中，支持对签署截止日期进行延期操作，主要涉及以下两个维度：
        1. 合同（流程）维度：只需要传递签署流程ID。这将对签署流程和发起时未单独设定签署截止时间的签署人进行延期操作。
        2. 签署人维度：需要传递流程ID和签署人ID。此操作将对签署人进行延期操作，尤其对于有序的合同（流程），签署截止时间不能超过后一位合同（流程）签署人的流程截止时间。

        此接口有如下限制条件：
        1. 执行操作的员工需为发起方企业的超级管理员、法定代表人或签署流程的发起人。
        2. 在延长整个签署流程时，签署流程应至少还有一方未签署（即签署流程不能处于已全部签署完成、已拒签、已过期、已撤回、拒绝填写、已解除等合同状态）。
        3. 在延长整个签署流程时，新的签署截止日期应晚于合同已设定的签署截止日期和当前日期。
        4. 在延长签署方的截止时间时，签署方不能处于流程完结或已终止状态（即签署人不能处于已签署、已拒签、已过期、已撤回、拒绝填写、已解除等状态）。
        5. 在延长签署方的截止时间时，签署方的新签署截止日期应晚于当前日期和签署方已设定的截止日期。若为有序合同，还应早于或等于下一签署人的截止日期，且早于签署流程整体的截止日期。
        6. 不支持操作合同组合同。

        :param request: Request instance for ModifyFlowDeadline.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.ModifyFlowDeadlineRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.ModifyFlowDeadlineResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyFlowDeadline", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyFlowDeadlineResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def OperateChannelTemplate(self, request):
        """此接口（OperateChannelTemplate）用于针对第三方应用平台模板库中的模板对子客企业发布授权的查询和设置。
        平台模板库中的模板的位置在控制台 企业应用管理 中下面的应用模板库管理目录, 可以参照下图位置
        ![image](https://qcloudimg.tencent-cloud.cn/raw/7f2b6c94164b3e931efc9a037e0400f7.png)

        # 支持的操作

        ## 1. 查询模板的子客企业授权 (OperateType=SELECT)
        - 查询模板的授权子企业列表

        ## 2. 修改模板的子客企业授权 (OperateType=UPDATE)
        - 当模板未发布时，可以修改模板的模板授权范围是**所有第三方应用合作企业**(AuthTag设置为all)或者**指定第三方应用合作企业**(AuthTag设置为part)，**当模板发布后，不可做此修改**
        - 如果模板是部分授权,  可通过ProxyOrganizationOpenIds增加子客的授权范围。

        ## 3. 取消模板的子客企业授权 (OperateType=DELETE)
        - 对子客企业进行模板库中模板授权范围的进行删除操作。
        - 主要对于手动领取的模板，去除授权后子客在模板库中看不到，就无法再领取了。但是**已经领取过成为自有模板的不会同步删除**。
        - 对于自动领取的模板，由于已经下发，更改授权不会影响。
        - 如果要同步删除子客自有模板库中的模板，请使用OperateType=UPDATE+Available参数处理。

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
        """此接口（SyncProxyOrganizationOperators）用于同步 第三方平台子客企业经办人列表，主要是同步经办人的离职状态。
        子客Web控制台的组织架构管理，依赖于第三方应用平台的，无法在页面针对员工做新增/更新/离职等操作， 必须通过 API 来操作。

        - **新增员工的场景**:    通过本接口提前导入员工列表, 然后调用<a href="https://qian.tencent.com/developers/partnerApis/accounts/CreateConsoleLoginUrl" target="_blank">生成子客登录链接</a>分享给对应的员工进行实名, 新增员工后员工的状态为**未实名**, 通过链接实名后状态变为**已实名**, 已实名员工就可以参与合同的发起。

        - **员工离职的场景**: 通过本接口将员工置为离职, 员工无法登录控制台和腾讯电子签小程序进行操作了,   同时给此员工分配的openid会被回收可以给其他新员工使用 (离职后员工数据会被置空,  再次加入公司会从零开始) ,  若员工信息有误可通过离职后在新增来解决,  离职员工状态为**离职**。

        ![image](https://qcloudimg.tencent-cloud.cn/raw/7a27a6bb0e4d39c2f6aa2a0b39946181/channel_SyncProxyOrganizationOperators.png)

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
        2. <font color='red'>此接口调用时需要单独设置Domain请求域名 </font>,  联调开发环境为 <font color='red'>file.test.ess.tencent.cn</font>，正式环境需要设置为<font color='red'>file.ess.tencent.cn</font>，代码示例
        ```
        HttpProfile httpProfile = new HttpProfile();
        httpProfile.setEndpoint("file.test.ess.tencent.cn");
        ```

        <font color="red">相关视频指引</font> <br>
        1. <a href="https://dyn.ess.tencent.cn/guide/apivideo/essbasic-UploadFiles.mp4" target="_blank">【上传文件代码】编写示例</a><br>

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