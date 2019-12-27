# -*- coding: utf-8 -*-
from tencentcloud.common import credential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
# 导入对应产品模块的client models。
from tencentcloud.sms.v20190711 import sms_client, models

# 导入可选配置类
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
try:
    # 必要步骤：
    # 实例化一个认证对象，入参需要传入腾讯云账户密钥对secretId，secretKey。
    # 这里采用的是从环境变量读取的方式，需要在环境变量中先设置这两个值。
    # 你也可以直接在代码中写死密钥对，但是小心不要将代码复制、上传或者分享给他人，
    # 以免泄露密钥对危及你的财产安全。
    # CAM密匙查询: https://console.cloud.tencent.com/cam/capi
    cred = credential.Credential("secretId", "secretKey")
    # cred = credential.Credential(
    #     os.environ.get(""),
    #     os.environ.get("")
    # )

    # 实例化一个http选项，可选的，没有特殊需求可以跳过。
    httpProfile = HttpProfile()
    httpProfile.reqMethod = "POST"  # post请求(默认为post请求)
    httpProfile.reqTimeout = 30    # 请求超时时间，单位为秒(默认60秒)
    httpProfile.endpoint = "sms.tencentcloudapi.com"  # 指定接入地域域名(默认就近接入)

    # 非必要步骤:
    # 实例化一个客户端配置对象，可以指定超时时间等配置
    clientProfile = ClientProfile()
    clientProfile.signMethod = "TC3-HMAC-SHA256"  # 指定签名算法
    clientProfile.language = "en-US"
    clientProfile.httpProfile = httpProfile

    # 实例化要请求产品(以sms为例)的client对象
    # 第二个参数是地域信息，可以直接填写字符串ap-guangzhou，或者引用预设的常量
    client = sms_client.SmsClient(cred, "ap-guangzhou", clientProfile)

    # 实例化一个请求对象，根据调用的接口和实际情况，可以进一步设置请求参数
    # 你可以直接查询SDK源码确定SendSmsRequest有哪些属性可以设置
    # 属性可能是基本类型，也可能引用了另一个数据结构
    # 推荐使用IDE进行开发，可以方便的跳转查阅各个接口和数据结构的文档说明
    req = models.SendSmsRequest()

    # 基本类型的设置:
    # SDK采用的是指针风格指定参数，即使对于基本类型你也需要用指针来对参数赋值。
    # SDK提供对基本类型的指针引用封装函数
    # 帮助链接：
    # 短信控制台: https://console.cloud.tencent.com/sms/smslist
    # sms helper: https://cloud.tencent.com/document/product/382/3773

    # 短信应用ID: 短信SdkAppid在 [短信控制台] 添加应用后生成的实际SdkAppid，示例如1400006666
    req.SmsSdkAppid = "1400787878"
    # 短信签名内容: 使用 UTF-8 编码，必须填写已审核通过的签名，签名信息可登录 [短信控制台] 查看
    req.Sign = "xxx"
    # 短信码号扩展号: 默认未开通，如需开通请联系 [sms helper]
    req.ExtendCode = ""
    # 用户的 session 内容: 可以携带用户侧 ID 等上下文信息，server 会原样返回
    req.SessionContext = "xxx"
    # 国际/港澳台短信 senderid: 国内短信填空，默认未开通，如需开通请联系 [sms helper]
    req.SenderId = ""
    # 下发手机号码，采用 e.164 标准，+[国家或地区码][手机号]
    # 示例如：+8613711112222， 其中前面有一个+号 ，86为国家码，13711112222为手机号，最多不要超过200个手机号
    req.PhoneNumberSet = ["+8613711112222"]
    # 模板 ID: 必须填写已审核通过的模板 ID。模板ID可登录 [短信控制台] 查看
    req.TemplateID = "449739"
    # 模板参数: 若无模板参数，则设置为空
    req.TemplateParamSet = ["666"]


    # 通过client对象调用DescribeInstances方法发起请求。注意请求方法名与请求对象是对应的。
    # 返回的resp是一个DescribeInstancesResponse类的实例，与请求对象对应。
    resp = client.SendSms(req)

    # 输出json格式的字符串回包
    print(resp.to_json_string(indent=2))

except TencentCloudSDKException as err:
    print(err)
