# -*- coding: utf-8 -*-


class TencentCloudSDKException(Exception):
    """tencentcloudapi sdk 异常类"""

    def __init__(self, code=None, message=None, requestId=None):
        self.code = code
        self.message = message
        self.requestId = requestId

    def __str__(self):
        return "[TencentCloudSDKException] code:%s message:%s requestId:%s" % (
            self.code, self.message, self.requestId)

    def get_code(self):
        return self.code

    def get_message(self):
        return self.message

    def get_request_id(self):
        return self.requestId
