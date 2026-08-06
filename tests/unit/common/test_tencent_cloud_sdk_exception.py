from tencentcloud.common.exception import TencentCloudSDKException


def test_tencent_cloud_sdk_exception_get():
    exception = TencentCloudSDKException("code", "message", "requestId")
    assert exception.get_code() == "code"
    assert exception.get_message() == "message"
    assert exception.get_request_id() == "requestId"

    assert exception.__str__() == "[TencentCloudSDKException] code:code message:message requestId:requestId"
