# -*- coding: utf-8 -*-
import json
import os

import pytest

from contextlib import contextmanager
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.sts.v20180813 import sts_client, models
from tencentcloud.cvm.v20170312 import cvm_client
from tencentcloud.cvm.v20170312 import models as cvm_models
from tencentcloud.common.credential import STSAssumeRoleCredential, OIDCRoleArnCredential, DefaultTkeOIDCRoleArnProvider

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


# patch requests.Session.request to get underlying request we send
@contextmanager
def mock_requests():
    import requests
    real_request = requests.Session.request

    req_args = {}

    def interceptor(self, method, url, **kwargs):
        req_args["self"] = self
        req_args["method"] = method
        req_args["url"] = url
        req_args.update(kwargs)
        return real_request(self, method, url, **kwargs)

    requests.Session.request = interceptor

    yield req_args

    requests.Session.request = real_request


def parse_host(url):
    try:
        from urlparse import urlparse  # Python 2
    except ImportError:
        from urllib.parse import urlparse  # Python 3
    return urlparse(url).hostname


def test_sts_credential_with_default_endpoint():
    expected_host = "sts.tencentcloudapi.com"

    cred = STSAssumeRoleCredential(
        "test-secret-id",
        "test-secret-key",
        "test-role-arn",
        "test-role-session-name",
        7000
    )

    with mock_requests() as req_args:
        try:
            cred.get_sts_tmp_role_arn()
        except TencentCloudSDKException:
            pass

        assert parse_host(req_args["url"]) == expected_host


def test_sts_credential_with_set_endpoint():
    expected_host = "sts.internal.tencentcloudapi.com"

    cred = STSAssumeRoleCredential(
        "test-secret-id",
        "test-secret-key",
        "test-role-arn",
        "test-role-session-name",
        7000,
        "sts.internal.tencentcloudapi.com"
    )

    with mock_requests() as req_args:
        try:
            cred.get_sts_tmp_role_arn()
        except TencentCloudSDKException:
            pass

        assert parse_host(req_args["url"]) == expected_host


def test_oidc_credential_with_deault_endpoint():
    expected_host = "sts.tencentcloudapi.com"

    cred = OIDCRoleArnCredential(
        region="test-region",
        provider_id="test-provider-id",
        web_identity_token="test-web-identity-token",
        role_arn="test-role-arn",
        role_session_name="test-role-session-name"
    )

    with mock_requests() as req_args:
        try:
            cred.refresh()
        except TencentCloudSDKException:
            pass

        assert parse_host(req_args["url"]) == expected_host


def test_oidc_credential_with_set_endpoint():
    expected_host = "sts.internal.tencentcloudapi.com"

    cred = OIDCRoleArnCredential(
        region="test-region",
        provider_id="test-provider-id",
        web_identity_token="test-web-identity-token",
        role_arn="test-role-arn",
        role_session_name="test-role-session-name",
        endpoint="sts.internal.tencentcloudapi.com" 
    )

    with mock_requests() as req_args:
        try:
            cred.refresh()
        except TencentCloudSDKException:
            pass

        assert parse_host(req_args["url"]) == expected_host


def test_tke_oidc_credential_with_default_endpoint():
    import tempfile

    expected_host = "sts.tencentcloudapi.com"

    os.environ["TKE_REGION"] = "test_tke"
    os.environ["TKE_PROVIDER_ID"] = "test_tke"
    os.environ["TKE_ROLE_ARN"] = "test_tke"

    with tempfile.NamedTemporaryFile(mode="w+") as f:
        os.environ["TKE_WEB_IDENTITY_TOKEN_FILE"] = f.name
        cred = DefaultTkeOIDCRoleArnProvider().get_credential()

        with mock_requests() as req_args:
            try:
                cred.refresh()
            except TencentCloudSDKException:
                pass

            assert parse_host(req_args["url"]) == expected_host


def test_tke_oidc_credential_with_set_endpoint():
    import tempfile

    expected_host = "sts.internal.tencentcloudapi.com"

    os.environ["TKE_REGION"] = "test_tke"
    os.environ["TKE_PROVIDER_ID"] = "test_tke"
    os.environ["TKE_ROLE_ARN"] = "test_tke"

    with tempfile.NamedTemporaryFile(mode="w+") as f:
        os.environ["TKE_WEB_IDENTITY_TOKEN_FILE"] = f.name
        cred = DefaultTkeOIDCRoleArnProvider().get_credential()
        cred.endpoint = "sts.internal.tencentcloudapi.com"

        with mock_requests() as req_args:
            try:
                cred.refresh()
            except TencentCloudSDKException:
                pass

            assert parse_host(req_args["url"]) == expected_host
