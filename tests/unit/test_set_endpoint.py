# -*- coding: utf-8 -*-
from contextlib import contextmanager
from urllib.parse import urlparse

import os
import requests
import tempfile

from tencentcloud.common.exception import TencentCloudSDKException
from tencentcloud.common.credential import STSAssumeRoleCredential, OIDCRoleArnCredential, DefaultTkeOIDCRoleArnProvider


@contextmanager
def mock_requests():
    real_request = requests.Session.request
    req_args = {}

    def interceptor(self, method, url, **kwargs):
        req_args["method"] = method
        req_args["url"] = url
        return real_request(self, method, url, **kwargs)

    requests.Session.request = interceptor

    yield req_args
    
    requests.Session.request = real_request


def parse_host(url):
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
    expected_host = "sts.tencentcloudapi.com"

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
    expected_host = "sts.internal.tencentcloudapi.com"

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
