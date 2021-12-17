# -*- coding: utf-8 -*-
import json
import os
from itertools import product
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.cvm.v20170312 import cvm_client, models

signmethod_list = ['HmacSHA256', 'HmacSHA1']
reqmethod_list = ['GET', 'POST']


def test_signature_v1_ok():
    for signmethod, reqmethod in product(signmethod_list, reqmethod_list):
        cred = credential.Credential(
            os.environ.get("TENCENTCLOUD_SECRET_ID"),
            os.environ.get("TENCENTCLOUD_SECRET_KEY"))
        httpProfile = HttpProfile()
        httpProfile.endpoint = "cvm.tencentcloudapi.com"
        httpProfile.reqMethod = reqmethod

        clientProfile = ClientProfile()
        clientProfile.signMethod = signmethod
        clientProfile.httpProfile = httpProfile
        client = cvm_client.CvmClient(cred, "ap-guangzhou", clientProfile)

        req = models.DescribeZonesRequest()
        resp = client.DescribeZones(req)


def test_signature_v1_fail():
    for signmethod, reqmethod in product(signmethod_list, reqmethod_list):
        cred = credential.Credential(
            os.environ.get("TENCENTCLOUD_SECRET_ID"),
            os.environ.get("TENCENTCLOUD_SECRET_KEY"))
        httpProfile = HttpProfile()
        httpProfile.endpoint = "cvm.tencentcloudapi.com"
        httpProfile.reqMethod = reqmethod

        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        client = cvm_client.CvmClient(cred, "ap-guangzhou", clientProfile)

        req = models.DescribeInstancesOperationLimitRequest()
        params = {
            "InstanceIds": [""],
            "Operation": "INSTANCE_DEGRADE"
        }
        req.from_json_string(json.dumps(params))
        try:
            resp = client.DescribeInstancesOperationLimit(req)
            assert False, 'unexpected success, should fail'
        except TencentCloudSDKException as err:
            assert err.code == 'InvalidInstanceId.Malformed'
