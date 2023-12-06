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
from tencentcloud.gme.v20180711 import models


class GmeClient(AbstractClient):
    _apiVersion = '2018-07-11'
    _endpoint = 'gme.tencentcloudapi.com'
    _service = 'gme'


    def CreateAgeDetectTask(self, request):
        """目前该功能底层能力已不具备，不对外提供，目前需要下线，走预下线流程。

        用于创建年龄语音识别任务的接口，请求频率10次/秒。该接口目前通过白名单开放试用，如有需求，请提交工单申请。
        </br>
        <h4><b>接口功能说明：</b></h4>
        <li>支持对语音文件进行检测，判断是否为未成年人。</li>
        <li>支持批量提交检测子任务。检测子任务列表最多支持100个。</li>
        </br>
        <h4><b>音频文件限制说明：</b></h4>
        <li>音频文件大小限制：10 M</li>
        <li>音频文件时长限制：3分钟</li>
        <li>音频文件格式支持的类型：.wav、.m4a、.amr、.mp3、.aac、.wma、.ogg</li>
        </br>

        :param request: Request instance for CreateAgeDetectTask.
        :type request: :class:`tencentcloud.gme.v20180711.models.CreateAgeDetectTaskRequest`
        :rtype: :class:`tencentcloud.gme.v20180711.models.CreateAgeDetectTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAgeDetectTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAgeDetectTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateApp(self, request):
        """本接口(CreateApp)用于创建一个GME应用。

        :param request: Request instance for CreateApp.
        :type request: :class:`tencentcloud.gme.v20180711.models.CreateAppRequest`
        :rtype: :class:`tencentcloud.gme.v20180711.models.CreateAppResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateApp", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAppResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCustomization(self, request):
        """用户使用该接口可以创建语音消息转文本热句模型，以供识别调用

        :param request: Request instance for CreateCustomization.
        :type request: :class:`tencentcloud.gme.v20180711.models.CreateCustomizationRequest`
        :rtype: :class:`tencentcloud.gme.v20180711.models.CreateCustomizationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCustomization", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCustomizationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateScanUser(self, request):
        """新增自定义送检用户。**接口使用前提**：目前 CreateScanUser 接口通过白名单开放，如需使用，需要 [提交工单申请](https://console.cloud.tencent.com/workorder/category?level1_id=438&level2_id=445&source=0&data_title=%E6%B8%B8%E6%88%8F%E5%A4%9A%E5%AA%92%E4%BD%93%E5%BC%95%E6%93%8EGME&step=1)。

        :param request: Request instance for CreateScanUser.
        :type request: :class:`tencentcloud.gme.v20180711.models.CreateScanUserRequest`
        :rtype: :class:`tencentcloud.gme.v20180711.models.CreateScanUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateScanUser", params, headers=headers)
            response = json.loads(body)
            model = models.CreateScanUserResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCustomization(self, request):
        """用户通过该接口可以删除语音消息转文本热句模型

        :param request: Request instance for DeleteCustomization.
        :type request: :class:`tencentcloud.gme.v20180711.models.DeleteCustomizationRequest`
        :rtype: :class:`tencentcloud.gme.v20180711.models.DeleteCustomizationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCustomization", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCustomizationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteRoomMember(self, request):
        """本接口(DeleteRoomMember)用户删除房间或者剔除房间内用户

        :param request: Request instance for DeleteRoomMember.
        :type request: :class:`tencentcloud.gme.v20180711.models.DeleteRoomMemberRequest`
        :rtype: :class:`tencentcloud.gme.v20180711.models.DeleteRoomMemberResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRoomMember", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteRoomMemberResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteScanUser(self, request):
        """删除自定义送检用户。**接口使用前提**：目前 DeleteScanUser 接口通过白名单开放，如需使用，需要 [提交工单申请](https://console.cloud.tencent.com/workorder/category?level1_id=438&level2_id=445&source=0&data_title=%E6%B8%B8%E6%88%8F%E5%A4%9A%E5%AA%92%E4%BD%93%E5%BC%95%E6%93%8EGME&step=1)。

        :param request: Request instance for DeleteScanUser.
        :type request: :class:`tencentcloud.gme.v20180711.models.DeleteScanUserRequest`
        :rtype: :class:`tencentcloud.gme.v20180711.models.DeleteScanUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteScanUser", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteScanUserResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAgeDetectTask(self, request):
        """目前该功能底层能力已不具备，不对外提供，目前需要下线，走预下线流程。

        查询年龄语音识别任务结果，请求频率10次/秒。该接口目前通过白名单开放试用，如有需求，请提交工单申请。

        :param request: Request instance for DescribeAgeDetectTask.
        :type request: :class:`tencentcloud.gme.v20180711.models.DescribeAgeDetectTaskRequest`
        :rtype: :class:`tencentcloud.gme.v20180711.models.DescribeAgeDetectTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAgeDetectTask", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAgeDetectTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAppStatistics(self, request):
        """本接口(DescribeAppStatistics)用于获取某个GME应用的用量数据。包括实时语音，语音消息及转文本，语音分析等。最长查询周期为最近60天。

        :param request: Request instance for DescribeAppStatistics.
        :type request: :class:`tencentcloud.gme.v20180711.models.DescribeAppStatisticsRequest`
        :rtype: :class:`tencentcloud.gme.v20180711.models.DescribeAppStatisticsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAppStatistics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAppStatisticsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeApplicationData(self, request):
        """本接口(DescribeApplicationData)用于获取数据详情信息，最多可拉取最近90天的数据。

        :param request: Request instance for DescribeApplicationData.
        :type request: :class:`tencentcloud.gme.v20180711.models.DescribeApplicationDataRequest`
        :rtype: :class:`tencentcloud.gme.v20180711.models.DescribeApplicationDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeApplicationData", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeApplicationDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeApplicationList(self, request):
        """本接口(DescribeApplicationList)用于查询自己账号下的应用列表

        :param request: Request instance for DescribeApplicationList.
        :type request: :class:`tencentcloud.gme.v20180711.models.DescribeApplicationListRequest`
        :rtype: :class:`tencentcloud.gme.v20180711.models.DescribeApplicationListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeApplicationList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeApplicationListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRealtimeScanConfig(self, request):
        """获取用户自定义送检信息。**接口使用前提**：目前 DescribeRealtimeScanConfig 接口通过白名单开放，如需使用，需要 [提交工单申请](https://console.cloud.tencent.com/workorder/category?level1_id=438&level2_id=445&source=0&data_title=%E6%B8%B8%E6%88%8F%E5%A4%9A%E5%AA%92%E4%BD%93%E5%BC%95%E6%93%8EGME&step=1)。

        :param request: Request instance for DescribeRealtimeScanConfig.
        :type request: :class:`tencentcloud.gme.v20180711.models.DescribeRealtimeScanConfigRequest`
        :rtype: :class:`tencentcloud.gme.v20180711.models.DescribeRealtimeScanConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRealtimeScanConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRealtimeScanConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRecordInfo(self, request):
        """查询录制任务信息。

        :param request: Request instance for DescribeRecordInfo.
        :type request: :class:`tencentcloud.gme.v20180711.models.DescribeRecordInfoRequest`
        :rtype: :class:`tencentcloud.gme.v20180711.models.DescribeRecordInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRecordInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRecordInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRoomInfo(self, request):
        """获取房间内用户信息

        :param request: Request instance for DescribeRoomInfo.
        :type request: :class:`tencentcloud.gme.v20180711.models.DescribeRoomInfoRequest`
        :rtype: :class:`tencentcloud.gme.v20180711.models.DescribeRoomInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRoomInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRoomInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeScanResultList(self, request):
        """本接口(DescribeScanResultList)用于查询语音检测结果，查询任务列表最多支持100个。
        <p style="color:red">如果在提交语音检测任务时未设置 Callback 字段，则需要通过本接口获取检测结果</p>

        :param request: Request instance for DescribeScanResultList.
        :type request: :class:`tencentcloud.gme.v20180711.models.DescribeScanResultListRequest`
        :rtype: :class:`tencentcloud.gme.v20180711.models.DescribeScanResultListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeScanResultList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeScanResultListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTaskInfo(self, request):
        """查询房间录制的详细信息

        :param request: Request instance for DescribeTaskInfo.
        :type request: :class:`tencentcloud.gme.v20180711.models.DescribeTaskInfoRequest`
        :rtype: :class:`tencentcloud.gme.v20180711.models.DescribeTaskInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTaskInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTaskInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUserInAndOutTime(self, request):
        """拉取用户在房间得进出时间

        :param request: Request instance for DescribeUserInAndOutTime.
        :type request: :class:`tencentcloud.gme.v20180711.models.DescribeUserInAndOutTimeRequest`
        :rtype: :class:`tencentcloud.gme.v20180711.models.DescribeUserInAndOutTimeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUserInAndOutTime", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUserInAndOutTimeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetCustomizationList(self, request):
        """查询语音消息转文本热句模型列表

        :param request: Request instance for GetCustomizationList.
        :type request: :class:`tencentcloud.gme.v20180711.models.GetCustomizationListRequest`
        :rtype: :class:`tencentcloud.gme.v20180711.models.GetCustomizationListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetCustomizationList", params, headers=headers)
            response = json.loads(body)
            model = models.GetCustomizationListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAppStatus(self, request):
        """本接口(ModifyAppStatus)用于修改应用总开关状态。

        :param request: Request instance for ModifyAppStatus.
        :type request: :class:`tencentcloud.gme.v20180711.models.ModifyAppStatusRequest`
        :rtype: :class:`tencentcloud.gme.v20180711.models.ModifyAppStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAppStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAppStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCustomization(self, request):
        """用户通过该接口可以更新语音消息转文本热句模型。

        :param request: Request instance for ModifyCustomization.
        :type request: :class:`tencentcloud.gme.v20180711.models.ModifyCustomizationRequest`
        :rtype: :class:`tencentcloud.gme.v20180711.models.ModifyCustomizationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCustomization", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCustomizationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCustomizationState(self, request):
        """通过该接口，用户可以修改语音消息转文本热句模型状态，上下线热句模型

        :param request: Request instance for ModifyCustomizationState.
        :type request: :class:`tencentcloud.gme.v20180711.models.ModifyCustomizationStateRequest`
        :rtype: :class:`tencentcloud.gme.v20180711.models.ModifyCustomizationStateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCustomizationState", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCustomizationStateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyRecordInfo(self, request):
        """修改录制配置信息

        :param request: Request instance for ModifyRecordInfo.
        :type request: :class:`tencentcloud.gme.v20180711.models.ModifyRecordInfoRequest`
        :rtype: :class:`tencentcloud.gme.v20180711.models.ModifyRecordInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRecordInfo", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyRecordInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyUserMicStatus(self, request):
        """**接口作用**：此接口用于修改房间用户的麦克风状态，例如房间内用户麦克风为打开状态，可调用此接口将该用户麦克风进行关闭，关闭后即使该用户使用客户端接口 EnableMic 打开麦克风，依然无法与房间内成员通话，属于被禁言状态。该状态持续到此用户退房后失效，或者调用该接口重新打开此用户麦克风状态。
        **接口应用场景**：此接口多用于游戏业务中台或者风控后台，对一些发表不当言论的玩家进行禁言处理。
        **接口使用前提**：目前 ModifyUserMicStatus 接口通过白名单开放，如需使用，需要 [提交工单申请](https://console.cloud.tencent.com/workorder/category?level1_id=438&level2_id=445&source=0&data_title=%E6%B8%B8%E6%88%8F%E5%A4%9A%E5%AA%92%E4%BD%93%E5%BC%95%E6%93%8EGME&step=1)。

        :param request: Request instance for ModifyUserMicStatus.
        :type request: :class:`tencentcloud.gme.v20180711.models.ModifyUserMicStatusRequest`
        :rtype: :class:`tencentcloud.gme.v20180711.models.ModifyUserMicStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyUserMicStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyUserMicStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ScanVoice(self, request):
        """本接口(ScanVoice)用于提交语音检测任务，检测任务列表最多支持100个。使用前请您登录[控制台 - 服务配置](https://console.cloud.tencent.com/gamegme/conf)开启语音内容安全服务。
        </br></br>

        <h4><b>功能试用说明：</b></h4>
        <li>打开前往<a href="https://console.cloud.tencent.com/gamegme/tryout">控制台 - 产品试用</a>免费试用语音内容安全服务。</li>
        </br>

        <h4><b>接口功能说明：</b></h4>
        <li>支持对语音流或语音文件进行检测，判断其中是否包含违规内容。</li>
        <li>支持设置回调地址 Callback 获取检测结果，同时支持通过接口(查询语音检测结果)主动轮询获取检测结果。</li>
        <li>支持场景输入，包括：谩骂、色情等场景</li>
        <li>支持批量提交检测任务。检测任务列表最多支持100个。</li>
        </br>
        <h4><b>音频文件限制说明：</b></h4>
        <li>音频文件大小限制：100 M</li>
        <li>音频文件时长限制：30分钟</li>
        <li>音频文件格式支持的类型：.wav、.m4a、.amr、.mp3、.aac、.wma、.ogg</li>
        </br>
        <h4><b>语音流限制说明：</b></h4>
        <li>语音流格式支持的类型：.m3u8、.flv</li>
        <li>语音流支持的传输协议：RTMP、HTTP、HTTPS</li>
        <li>语音流时长限制：4小时</li>
        <li>支持音视频流分离并对音频流进行分析</li>
        </br>
        <h4 id="Label_Value"><b>Scenes 与 Label 参数说明：</b></h4>
        <p>提交语音检测任务时，需要指定 Scenes 场景参数，<font color="red">目前要求您设置 Scenes 参数值为：["default"]</font>；而在检测结果中，则包含请求时指定的场景，以及对应类型的检测结果。</p>
        <table>
        <thread>
        <tr>
        <th>场景</th>
        <th>描述</th>
        <th>Label</th>
        </tr>
        </thread>
        <tbody>
        <tr>
        <td>语音检测</td>
        <td>语音检测的检测类型</td>
        <td>
        <p>normal:正常文本</p>
        <p>porn:色情</p>
        <p>abuse:谩骂</p>
        <p>ad :广告</p>
        <p>illegal :违法</p>
        <p>moan :呻吟</p>
        <p>customized:自定义词库</p>
        </td>
        </tr>
        </tbody>
        </table>
        </br>
        <h4 id="Callback_Declare"><b>回调相关说明：</b></h4>
        <li>如果在请求参数中指定了回调地址参数 Callback，即一个 HTTP(S) 协议接口的 URL，则需要支持 POST 方法，传输数据编码采用 UTF-8。</li>
        <li>在推送回调数据后，接收到的 HTTP 状态码为 200 时，表示推送成功。</li>
        <li>HTTP 请求参数（query）说明：</li>
        <table>
        <thread>
        <tr>
        <th>名称</th>
        <th>类型</th>
        <th>是否必需</th>
        <th>描述</th>
        </tr>
        </thread>
        <tbody>
        <tr>
        <td>Signatue</td>
        <td>string</td>
        <td>是</td>
        <td>签名，具体见<a href="#Callback_Signatue">签名生成说明</a></td>
        </tr>
        </tbody>
        </table>
        <ul  id="Callback_Signatue">
        	<li>签名生成说明：</li>
        	<ul>
        		<li>使用 HMAC-SH1 算法, 最终结果做 BASE64 编码;</li>
        		<li>签名原文串为 POST+body 的整个json内容(长度以 Content-Length 为准);</li>
        		<li>签名key为应用的 SecretKey，可以通过控制台查看。</li>
        	</ul>
        </ul>

        <li>回调示例如下<font color="red">（详细字段说明见结构：
        <a href="https://cloud.tencent.com/document/api/607/35375#DescribeScanResult" target="_blank">DescribeScanResult</a>）</font>：</li>
        <pre><code>{
        	"Code": 0,
        	"DataId": "1400000000_test_data_id",
        	"ScanFinishTime": 1566720906,
        	"HitFlag": true,
        	"Live": false,
        	"Msg": "",
        	"ScanPiece": [{
        		"DumpUrl": "",
        		"HitFlag": true,
        		"MainType": "abuse",
        		"RoomId": "123",
        		"OpenId": "111",
        		"Info":"",
        		"Offset": 0,
        		"Duration": 3400,
        		"PieceStartTime":1574684231,
        		"ScanDetail": [{
        			"EndTime": 1110,
        			"KeyWord": "违规字",
        			"Label": "abuse",
        			"Rate": "90.00",
        			"StartTime": 1110
        		}, {
        			"EndTime": 1380,
        			"KeyWord": "违规字",
        			"Label": "abuse",
        			"Rate": "90.00",
        			"StartTime": 930
        		}, {
        			"EndTime": 1560,
        			"KeyWord": "违规字",
        			"Label": "abuse",
        			"Rate": "90.00",
        			"StartTime": 930
        		}, {
        			"EndTime": 2820,
        			"KeyWord": "违规字",
        			"Label": "abuse",
        			"Rate": "90.00",
        			"StartTime": 2490
        		}]
        	}],
        	"ScanStartTime": 1566720905,
        	"Scenes": [
        		"default"
        	],
        	"Status": "Success",
        	"TaskId": "6330xxxx-9xx7-11ed-98e3-52xxxxe4ac3b",
        	"Url": "https://xxx/xxx.m4a"
        }
        </code></pre>

        :param request: Request instance for ScanVoice.
        :type request: :class:`tencentcloud.gme.v20180711.models.ScanVoiceRequest`
        :rtype: :class:`tencentcloud.gme.v20180711.models.ScanVoiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ScanVoice", params, headers=headers)
            response = json.loads(body)
            model = models.ScanVoiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StartRecord(self, request):
        """开启录制

        :param request: Request instance for StartRecord.
        :type request: :class:`tencentcloud.gme.v20180711.models.StartRecordRequest`
        :rtype: :class:`tencentcloud.gme.v20180711.models.StartRecordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StartRecord", params, headers=headers)
            response = json.loads(body)
            model = models.StartRecordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopRecord(self, request):
        """停止录制

        :param request: Request instance for StopRecord.
        :type request: :class:`tencentcloud.gme.v20180711.models.StopRecordRequest`
        :rtype: :class:`tencentcloud.gme.v20180711.models.StopRecordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopRecord", params, headers=headers)
            response = json.loads(body)
            model = models.StopRecordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateScanRooms(self, request):
        """更新自定义送检房间号。**接口使用前提**：目前 UpdateScanRooms 接口通过白名单开放，如需使用，需要 [提交工单申请](https://console.cloud.tencent.com/workorder/category?level1_id=438&level2_id=445&source=0&data_title=%E6%B8%B8%E6%88%8F%E5%A4%9A%E5%AA%92%E4%BD%93%E5%BC%95%E6%93%8EGME&step=1)。

        :param request: Request instance for UpdateScanRooms.
        :type request: :class:`tencentcloud.gme.v20180711.models.UpdateScanRoomsRequest`
        :rtype: :class:`tencentcloud.gme.v20180711.models.UpdateScanRoomsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateScanRooms", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateScanRoomsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateScanUsers(self, request):
        """更新自定义送检用户号。
        **接口使用前提**：目前 UpdateScanUsers 接口通过白名单开放，如需使用，需要 [提交工单申请](https://console.cloud.tencent.com/workorder/category?level1_id=438&level2_id=445&source=0&data_title=%E6%B8%B8%E6%88%8F%E5%A4%9A%E5%AA%92%E4%BD%93%E5%BC%95%E6%93%8EGME&step=1)。

        :param request: Request instance for UpdateScanUsers.
        :type request: :class:`tencentcloud.gme.v20180711.models.UpdateScanUsersRequest`
        :rtype: :class:`tencentcloud.gme.v20180711.models.UpdateScanUsersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateScanUsers", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateScanUsersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))