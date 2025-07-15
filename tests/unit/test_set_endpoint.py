# -*- coding: utf-8 -*-
from contextlib import contextmanager
from urllib.parse import urlparse

import requests

from tencentcloud.common.exception import TencentCloudSDKException
from tencentcloud.common.credential import OIDCRoleArnCredential, STSAssumeRoleCredential


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


def test_sts_endpoint_with_default_override():
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


def test_sts_endpoint_with_set_override():
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


def test_oidc_endpoint_with_deault_override():
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


def test_oidc_endpoint_with_set_override():
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

