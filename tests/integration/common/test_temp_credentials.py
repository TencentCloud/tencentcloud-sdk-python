# -*- coding: utf-8 -*-
import json
import os

import pytest

from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.sts.v20180813 import sts_client, models
from tencentcloud.cvm.v20170312 import cvm_client
from tencentcloud.cvm.v20170312 import models as cvm_models

reqmethod_list = ['GET', 'POST']


def _get_temp_redentials():
    try:
        cred = credential.Credential(
            os.environ.get("TENCENTCLOUD_SECRET_ID"),
            os.environ.get("TENCENTCLOUD_SECRET_KEY"))
        httpProfile = HttpProfile()
        httpProfile.endpoint = "sts.tencentcloudapi.com"

        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        client = sts_client.StsClient(cred, "ap-guangzhou", clientProfile)

        req = models.AssumeRoleRequest()
        params = {
            "RoleArn": os.environ.get("TENCENTCLOUD_ROLE_ARN"),
            "RoleSessionName": "cloudapi-test"
        }
        req.from_json_string(json.dumps(params))
        resp = client.AssumeRole(req)
        return resp.Credentials.TmpSecretId, resp.Credentials.TmpSecretKey, resp.Credentials.Token
    except TencentCloudSDKException as err:
        assert err.requestId is not None


@pytest.mark.skipif(not os.environ.get("TENCENTCLOUD_ROLE_ARN"),
                    reason="TENCENTCLOUD_ROLE_ARN env var not found")
def test_temp_credential_ok():
    temp_info = _get_temp_redentials()
    for reqmethod in reqmethod_list:
        temp_cred = credential.Credential(temp_info[0], temp_info[1], temp_info[2])
        httpProfile = HttpProfile()
        httpProfile.endpoint = "cvm.tencentcloudapi.com"
        httpProfile.reqMethod = reqmethod

        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        client = cvm_client.CvmClient(temp_cred, "ap-guangzhou", clientProfile)

        req = cvm_models.DescribeZonesRequest()
        resp = client.DescribeZones(req)


@pytest.mark.skipif(not os.environ.get("TENCENTCLOUD_ROLE_ARN"),
                    reason="TENCENTCLOUD_ROLE_ARN env var not found")
def test_temp_credential_invalid():
    temp_info = _get_temp_redentials()
    for reqmethod in reqmethod_list:
        invalid_cred = credential.Credential(temp_info[0], temp_info[1], temp_info[2] + 'err')
        httpProfile = HttpProfile()
        httpProfile.endpoint = "cvm.tencentcloudapi.com"
        httpProfile.reqMethod = reqmethod

        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        client = cvm_client.CvmClient(invalid_cred, "ap-guangzhou", clientProfile)

        req = cvm_models.DescribeInstancesOperationLimitRequest()
        params = {
            "InstanceIds": [""],
            "Operation": "INSTANCE_DEGRADE",
        }
        req.from_json_string(json.dumps(params))
        try:
            resp = client.DescribeInstancesOperationLimit(req)
        except TencentCloudSDKException as err:
            assert err.code == 'AuthFailure.TokenFailure'
