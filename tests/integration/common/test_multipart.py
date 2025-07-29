# -*- coding: utf-8 -*-
import json
import os

import pytest

from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.cvm.v20170312 import cvm_client
from tencentcloud.cvm.v20170312 import models as cvm_models


class CvmTest(cvm_client.CvmClient):

    def DescribeZones(self, request):
        try:
            params = request._serialize()
            options = {'IsMultipart': True}
            body = self.call("DescribeZones", params, options=options)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeZonesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


def test_json_action_with_multipart():
    try:
        cred = credential.Credential(
            os.environ.get("TENCENTCLOUD_SECRET_ID"),
            os.environ.get("TENCENTCLOUD_SECRET_KEY"))
        httpProfile = HttpProfile()
        httpProfile.endpoint = "cvm.tencentcloudapi.com"

        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile

        # overwrite client class, to enable multipart content type
        client = CvmTest(cred, "ap-guangzhou", clientProfile)

        req = cvm_models.DescribeZonesRequest()
        resp = client.DescribeZones(req)
        assert False, "unexpected success, should fail"
    except TencentCloudSDKException as err:
        assert u'not support Content-Type=`multipart/form-data`' in err.message
