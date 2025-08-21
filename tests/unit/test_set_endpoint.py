# -*- coding: utf-8 -*-
import os
from contextlib import contextmanager

from tencentcloud.common.exception import TencentCloudSDKException
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.credential import STSAssumeRoleCredential, OIDCRoleArnCredential, DefaultTkeOIDCRoleArnProvider


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
        "example#test#123456",
        "example#test#123456",
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
        "example#test#123456",
        "example#test#123456",
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
