# -*- coding: utf-8 -*-
import json
import os

from tencentcloud.common import credential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.cls.v20201016 import cls_client, models

# 1. 创建认证凭证（Credential）
# 从环境变量中获取密钥 ID 和密钥 Key，这是访问云 API 的必需凭证。
cred = credential.Credential(
    os.environ.get("TENCENTCLOUD_SECRET_ID"),
    os.environ.get("TENCENTCLOUD_SECRET_KEY"))

# 2. 创建客户端配置（ClientProfile）
cpf = ClientProfile()
cpf.httpProfile.reqTimeout = 300  # 流式接口可能耗时较长，因此将请求超时时间设置为 300 秒。
cpf.httpProfile.endpoint = "cls.ai.tencentcloudapi.com"  # 通过SSE流式调用此接口时，请务必设置请求域名（Endpoint）为 cls.ai.tencentcloudapi.com。
client = cls_client.ClsClient(cred, "ap-guangzhou", cpf)

# 3. 构造公共请求参数
msg = models.Message()
msg.Role = "user"
msg.Content = "状态码200, 统计日志条数"

meta_region = models.MetadataItem()
meta_region.Key = "topic_region"
meta_region.Value = "ap-guangzhou"
meta_topic = models.MetadataItem()
meta_topic.Key = "topic_id"
meta_topic.Value = "xxxxxxxx-xxxx"

# 4. 流式调用
# CLS ChatCompletions 同时支持流式和非流式两种模式。
# 将 Stream 参数设置为 True，表示以流式方式获取响应。
try:
    req = models.ChatCompletionsRequest()
    req.Model = "text2sql"
    req.Messages = [msg]
    req.Metadata = [meta_region, meta_topic]
    req.Stream = True
    resp = client.ChatCompletions(req)

    for event in resp:
        # 跳过心跳等 data 为空的事件（如服务端每隔一段时间发送的 :heartbeat 注释）
        if not event.get('data'):
            continue
        # 服务端通过 event: error 返回应用层错误
        if event.get("event") == "error":
            err = json.loads(event["data"])
            print("\n[流式] error", err["Response"]["Error"])
            continue
        data = json.loads(event['data'])
        for choice in data.get('Choices', []):
            # 实时输出思考过程（ReasoningContent）
            if choice['Delta'].get('ReasoningContent'):
                print(choice['Delta']['ReasoningContent'], end='', flush=True)
            # 实时输出回复内容（Content）
            if choice['Delta'].get('Content'):
                print(choice['Delta']['Content'], end='', flush=True)
    print()
    print('[流式] 完成，开始非流式调用...')

except TencentCloudSDKException as err:
    print("[流式] error", err)

# 5. 非流式调用
# 通过 Stream=False 参数来指定非 stream 协议，一次性拿到结果。
try:
    req = models.ChatCompletionsRequest()
    req.Model = "text2sql"
    req.Messages = [msg]
    req.Metadata = [meta_region, meta_topic]
    req.Stream = False
    resp = client.ChatCompletions(req)

    if resp.Choices[0].Message.ReasoningContent:
        print("思考过程：", resp.Choices[0].Message.ReasoningContent)
    print("[非流式] 回复内容：\n" + resp.Choices[0].Message.Content)

except TencentCloudSDKException as err:
    print("[非流式] error", err)
