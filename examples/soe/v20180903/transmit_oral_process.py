# -*- coding: utf-8 -*-

from tencentcloud.common import credential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
# 导入对应产品模块的client models。

from tencentcloud.soe.v20180724 import soe_client, models

from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile

try:
	# 实例化一个认证对象，入参需要传入腾讯云账户secretId，secretKey
	cred = credential.Credential("secretId", "secretKey")

	# 实例化一个http选项，可选的，没有特殊需求可以跳过。
	httpProfile = HttpProfile()
	httpProfile.reqMethod = "GET"  # post请求(默认为post请求)
	httpProfile.reqTimeout = 30  # 请求超时时间，单位为秒(默认60秒)
	httpProfile.endpoint = "soe.ap-shanghai.tencentcloudapi.com"  # 指定接入地域域名(默认就近接入)

	# 实例化一个client选项，可选的，没有特殊需求可以跳过。
	clientProfile = ClientProfile()
	clientProfile.signMethod = "HmacSHA256"  # 指定签名算法(默认为HmacSHA256)
	clientProfile.httpProfile = httpProfile

	client = soe_client.SoeClient(cred, "ap-shanghai", clientProfile)
	req = models.TransmitOralProcessRequest()
	req.SessionId = "stress_test_956938"
	req.VoiceFileType = 1
	req.SeqId = 1
	req.VoiceEncodeType = 1
	req.IsEnd = 0
	req.UserVoiceData = "VWtsR1JxeUpBd0JYUVZaRlptMTBJQkFBQUFBQkFBRUFnRDRBQUFCOUFBQUNBQkFBVEVsVFZCb0FBQUJKVGtaUFNWTkdWQTRBQUFCTVlYWm1OVFl1TVRrdU1UQXdBR1JoZEdGbWlRTUF5"

	resp = client.TransmitOralProcess(req)

	# 输出json格式的字符串回包
	print("%s" % resp.to_json_string())

except TencentCloudSDKException as err:
	print("%s" % err)
