# -*- coding: utf8 -*-
# Copyright (c) 2017-2025 Tencent. All Rights Reserved.
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



from tencentcloud.common.abstract_client_async import AbstractClient
from tencentcloud.gme.v20180711 import models
from typing import Dict


class GmeClient(AbstractClient):
    _apiVersion = '2018-07-11'
    _endpoint = 'gme.tencentcloudapi.com'
    _service = 'gme'

    async def ControlAIConversation(
            self,
            request: models.ControlAIConversationRequest,
            opts: Dict = None,
    ) -> models.ControlAIConversationResponse:
        """
        提供服务端控制机器人的功能
        """
        
        kwargs = {}
        kwargs["action"] = "ControlAIConversation"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ControlAIConversationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAgeDetectTask(
            self,
            request: models.CreateAgeDetectTaskRequest,
            opts: Dict = None,
    ) -> models.CreateAgeDetectTaskResponse:
        """
        目前该功能底层能力已不具备，不对外提供，目前需要下线，走预下线流程。

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
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAgeDetectTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAgeDetectTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateApp(
            self,
            request: models.CreateAppRequest,
            opts: Dict = None,
    ) -> models.CreateAppResponse:
        """
        本接口(CreateApp)用于创建一个GME应用。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateApp"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAppResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCustomization(
            self,
            request: models.CreateCustomizationRequest,
            opts: Dict = None,
    ) -> models.CreateCustomizationResponse:
        """
        用户使用该接口可以创建语音消息转文本热句模型，以供识别调用
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCustomization"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCustomizationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateScanUser(
            self,
            request: models.CreateScanUserRequest,
            opts: Dict = None,
    ) -> models.CreateScanUserResponse:
        """
        新增自定义送检用户。**接口使用前提**：目前 CreateScanUser 接口通过白名单开放，如需使用，需要 [提交工单申请](https://console.cloud.tencent.com/workorder/category?level1_id=438&level2_id=445&source=0&data_title=%E6%B8%B8%E6%88%8F%E5%A4%9A%E5%AA%92%E4%BD%93%E5%BC%95%E6%93%8EGME&step=1)。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateScanUser"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateScanUserResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCustomization(
            self,
            request: models.DeleteCustomizationRequest,
            opts: Dict = None,
    ) -> models.DeleteCustomizationResponse:
        """
        用户通过该接口可以删除语音消息转文本热句模型
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCustomization"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCustomizationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRoomMember(
            self,
            request: models.DeleteRoomMemberRequest,
            opts: Dict = None,
    ) -> models.DeleteRoomMemberResponse:
        """
        本接口(DeleteRoomMember)用户删除房间或者剔除房间内用户
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRoomMember"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRoomMemberResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteScanUser(
            self,
            request: models.DeleteScanUserRequest,
            opts: Dict = None,
    ) -> models.DeleteScanUserResponse:
        """
        删除自定义送检用户。**接口使用前提**：目前 DeleteScanUser 接口通过白名单开放，如需使用，需要 [提交工单申请](https://console.cloud.tencent.com/workorder/category?level1_id=438&level2_id=445&source=0&data_title=%E6%B8%B8%E6%88%8F%E5%A4%9A%E5%AA%92%E4%BD%93%E5%BC%95%E6%93%8EGME&step=1)。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteScanUser"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteScanUserResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteVoicePrint(
            self,
            request: models.DeleteVoicePrintRequest,
            opts: Dict = None,
    ) -> models.DeleteVoicePrintResponse:
        """
        传入声纹ID，删除之前注册的声纹信息
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteVoicePrint"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteVoicePrintResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAIConversation(
            self,
            request: models.DescribeAIConversationRequest,
            opts: Dict = None,
    ) -> models.DescribeAIConversationResponse:
        """
        查询AI对话任务状态。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAIConversation"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAIConversationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAgeDetectTask(
            self,
            request: models.DescribeAgeDetectTaskRequest,
            opts: Dict = None,
    ) -> models.DescribeAgeDetectTaskResponse:
        """
        目前该功能底层能力已不具备，不对外提供，目前需要下线，走预下线流程。

        查询年龄语音识别任务结果，请求频率10次/秒。该接口目前通过白名单开放试用，如有需求，请提交工单申请。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAgeDetectTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAgeDetectTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAppStatistics(
            self,
            request: models.DescribeAppStatisticsRequest,
            opts: Dict = None,
    ) -> models.DescribeAppStatisticsResponse:
        """
        本接口(DescribeAppStatistics)用于获取某个GME应用的用量数据。包括实时语音，语音消息及转文本，语音分析等。最长查询周期为最近60天。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAppStatistics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAppStatisticsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeApplicationData(
            self,
            request: models.DescribeApplicationDataRequest,
            opts: Dict = None,
    ) -> models.DescribeApplicationDataResponse:
        """
        本接口(DescribeApplicationData)用于获取数据详情信息，最多可拉取最近90天的数据。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeApplicationData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeApplicationDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeApplicationList(
            self,
            request: models.DescribeApplicationListRequest,
            opts: Dict = None,
    ) -> models.DescribeApplicationListResponse:
        """
        本接口(DescribeApplicationList)用于查询自己账号下的应用列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeApplicationList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeApplicationListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAuditResultExternal(
            self,
            request: models.DescribeAuditResultExternalRequest,
            opts: Dict = None,
    ) -> models.DescribeAuditResultExternalResponse:
        """
        获审核结果明细（外部API）
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAuditResultExternal"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAuditResultExternalResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRealtimeScanConfig(
            self,
            request: models.DescribeRealtimeScanConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeRealtimeScanConfigResponse:
        """
        获取用户自定义送检信息。**接口使用前提**：目前 DescribeRealtimeScanConfig 接口通过白名单开放，如需使用，需要 [提交工单申请](https://console.cloud.tencent.com/workorder/category?level1_id=438&level2_id=445&source=0&data_title=%E6%B8%B8%E6%88%8F%E5%A4%9A%E5%AA%92%E4%BD%93%E5%BC%95%E6%93%8EGME&step=1)。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRealtimeScanConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRealtimeScanConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRecordInfo(
            self,
            request: models.DescribeRecordInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeRecordInfoResponse:
        """
        查询录制任务信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRecordInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRecordInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRoomInfo(
            self,
            request: models.DescribeRoomInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeRoomInfoResponse:
        """
        获取房间内用户信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRoomInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRoomInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeScanResultList(
            self,
            request: models.DescribeScanResultListRequest,
            opts: Dict = None,
    ) -> models.DescribeScanResultListResponse:
        """
        本接口(DescribeScanResultList)用于查询语音检测结果，查询任务列表最多支持100个。
        <p style="color:red">如果在提交语音检测任务时未设置 Callback 字段，则需要通过本接口获取检测结果</p>
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeScanResultList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeScanResultListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTaskInfo(
            self,
            request: models.DescribeTaskInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeTaskInfoResponse:
        """
        查询房间录制的详细信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTaskInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTaskInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUserInAndOutTime(
            self,
            request: models.DescribeUserInAndOutTimeRequest,
            opts: Dict = None,
    ) -> models.DescribeUserInAndOutTimeResponse:
        """
        拉取用户在房间得进出时间
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUserInAndOutTime"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUserInAndOutTimeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVoicePrint(
            self,
            request: models.DescribeVoicePrintRequest,
            opts: Dict = None,
    ) -> models.DescribeVoicePrintResponse:
        """
        查询先前注册的声纹信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVoicePrint"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVoicePrintResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetCustomizationList(
            self,
            request: models.GetCustomizationListRequest,
            opts: Dict = None,
    ) -> models.GetCustomizationListResponse:
        """
        查询语音消息转文本热句模型列表
        """
        
        kwargs = {}
        kwargs["action"] = "GetCustomizationList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetCustomizationListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAppStatus(
            self,
            request: models.ModifyAppStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyAppStatusResponse:
        """
        本接口(ModifyAppStatus)用于修改应用总开关状态。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAppStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAppStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCustomization(
            self,
            request: models.ModifyCustomizationRequest,
            opts: Dict = None,
    ) -> models.ModifyCustomizationResponse:
        """
        用户通过该接口可以更新语音消息转文本热句模型。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCustomization"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCustomizationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCustomizationState(
            self,
            request: models.ModifyCustomizationStateRequest,
            opts: Dict = None,
    ) -> models.ModifyCustomizationStateResponse:
        """
        通过该接口，用户可以修改语音消息转文本热句模型状态，上下线热句模型
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCustomizationState"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCustomizationStateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRecordInfo(
            self,
            request: models.ModifyRecordInfoRequest,
            opts: Dict = None,
    ) -> models.ModifyRecordInfoResponse:
        """
        修改录制配置信息
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRecordInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRecordInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyUserMicStatus(
            self,
            request: models.ModifyUserMicStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyUserMicStatusResponse:
        """
        **接口作用**：此接口用于修改房间用户的麦克风状态，例如房间内用户麦克风为打开状态，可调用此接口将该用户麦克风进行关闭，关闭后即使该用户使用客户端接口 EnableMic 打开麦克风，依然无法与房间内成员通话，属于被禁言状态。该状态持续到此用户退房后失效，或者调用该接口重新打开此用户麦克风状态。
        **接口应用场景**：此接口多用于游戏业务中台或者风控后台，对一些发表不当言论的玩家进行禁言处理。
        **接口使用前提**：目前 ModifyUserMicStatus 接口通过白名单开放，如需使用，需要 [提交工单申请](https://console.cloud.tencent.com/workorder/category?level1_id=438&level2_id=445&source=0&data_title=%E6%B8%B8%E6%88%8F%E5%A4%9A%E5%AA%92%E4%BD%93%E5%BC%95%E6%93%8EGME&step=1)。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyUserMicStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyUserMicStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RegisterVoicePrint(
            self,
            request: models.RegisterVoicePrintRequest,
            opts: Dict = None,
    ) -> models.RegisterVoicePrintResponse:
        """
        传入音频base64串，注册声纹信息，返回声纹ID
        """
        
        kwargs = {}
        kwargs["action"] = "RegisterVoicePrint"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RegisterVoicePrintResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ScanVoice(
            self,
            request: models.ScanVoiceRequest,
            opts: Dict = None,
    ) -> models.ScanVoiceResponse:
        """
        本接口(ScanVoice)用于提交语音检测任务，检测任务列表最多支持100个。使用前请您登录[控制台 - 服务配置](https://console.cloud.tencent.com/gamegme/conf)开启语音内容安全服务。
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
        """
        
        kwargs = {}
        kwargs["action"] = "ScanVoice"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ScanVoiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StartAIConversation(
            self,
            request: models.StartAIConversationRequest,
            opts: Dict = None,
    ) -> models.StartAIConversationResponse:
        """
        启动AI对话任务，AI通道机器人进入GME房间，与房间内指定的成员进行AI对话，适用于智能客服，AI口语教师等场景

        GME AI对话功能内置语音转文本能力，同时提供通道服务，即客户可灵活指定第三方AI模型（LLM）服务和文本转音频（TTS）服务，更多[功能说明](https://cloud.tencent.com/document/product/647/108901)。
        """
        
        kwargs = {}
        kwargs["action"] = "StartAIConversation"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StartAIConversationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StartRecord(
            self,
            request: models.StartRecordRequest,
            opts: Dict = None,
    ) -> models.StartRecordResponse:
        """
        开启录制
        """
        
        kwargs = {}
        kwargs["action"] = "StartRecord"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StartRecordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopAIConversation(
            self,
            request: models.StopAIConversationRequest,
            opts: Dict = None,
    ) -> models.StopAIConversationResponse:
        """
        停止AI对话任务
        """
        
        kwargs = {}
        kwargs["action"] = "StopAIConversation"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopAIConversationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopRecord(
            self,
            request: models.StopRecordRequest,
            opts: Dict = None,
    ) -> models.StopRecordResponse:
        """
        停止录制
        """
        
        kwargs = {}
        kwargs["action"] = "StopRecord"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopRecordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateAIConversation(
            self,
            request: models.UpdateAIConversationRequest,
            opts: Dict = None,
    ) -> models.UpdateAIConversationResponse:
        """
        更新AIConversation参数
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateAIConversation"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateAIConversationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateScanRooms(
            self,
            request: models.UpdateScanRoomsRequest,
            opts: Dict = None,
    ) -> models.UpdateScanRoomsResponse:
        """
        更新自定义送检房间号。**接口使用前提**：目前 UpdateScanRooms 接口通过白名单开放，如需使用，需要 [提交工单申请](https://console.cloud.tencent.com/workorder/category?level1_id=438&level2_id=445&source=0&data_title=%E6%B8%B8%E6%88%8F%E5%A4%9A%E5%AA%92%E4%BD%93%E5%BC%95%E6%93%8EGME&step=1)。
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateScanRooms"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateScanRoomsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateScanUsers(
            self,
            request: models.UpdateScanUsersRequest,
            opts: Dict = None,
    ) -> models.UpdateScanUsersResponse:
        """
        更新自定义送检用户号。
        **接口使用前提**：目前 UpdateScanUsers 接口通过白名单开放，如需使用，需要 [提交工单申请](https://console.cloud.tencent.com/workorder/category?level1_id=438&level2_id=445&source=0&data_title=%E6%B8%B8%E6%88%8F%E5%A4%9A%E5%AA%92%E4%BD%93%E5%BC%95%E6%93%8EGME&step=1)。
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateScanUsers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateScanUsersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateVoicePrint(
            self,
            request: models.UpdateVoicePrintRequest,
            opts: Dict = None,
    ) -> models.UpdateVoicePrintResponse:
        """
        传入声纹ID以及对应音频信息，更新对应声纹信息
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateVoicePrint"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateVoicePrintResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)