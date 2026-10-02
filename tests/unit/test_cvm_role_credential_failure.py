# -*- coding: utf-8 -*-
import inspect
import sys
import warnings

import tencentcloud.common.credential as credential_module
from tencentcloud.common.credential import CVMRoleCredential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import (
    TencentCloudSDKException,
)


def test_no_return_in_finally_syntax_warning():
    # PEP 765: Python 3.14 emits SyntaxWarning at compile time for
    # return/break/continue in a finally block. The warning fires on import,
    # so strict environments (-W error) fail before any code runs.
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        compile(inspect.getsource(credential_module),
                credential_module.__file__, "exec")
    if sys.version_info < (3, 14):
        # the warning is introduced in 3.14; older interpreters emit nothing
        return
    syntax_warnings = [
        w for w in caught if issubclass(w.category, SyntaxWarning)
    ]
    assert len(syntax_warnings) == 0, \
        "unexpected SyntaxWarning: %s" % syntax_warnings[0].message


def _make_failing_role_urlopen(exc):
    def fake_urlopen(url, *args, **kwargs):
        raise exc

    return fake_urlopen


def _make_success_urlopen():
    class _Resp(object):
        def __init__(self, payload):
            self._payload = payload

        def read(self):
            return self._payload

    def fake_urlopen(url, *args, **kwargs):
        if url.endswith("/cam/security-credentials/"):
            return _Resp(b"mock-role")
        if url.endswith("/cam/security-credentials/mock-role"):
            import json
            data = {
                "TmpSecretId": "id-from-metadata",
                "TmpSecretKey": "key-from-metadata",
                "Token": "token-from-metadata",
                "ExpiredTime": 2147483647,
                "Code": "Success",
            }
            return _Resp(json.dumps(data).encode("utf-8"))
        raise Exception("Unexpected URL: {}".format(url))

    return fake_urlopen


def test_success_path_fills_credential_values():
    # a reachable metadata endpoint must fill the exact credential triple
    # (value-level check; the existing concurrency test only asserts the
    # three fields stay equal to each other)
    cred = CVMRoleCredential()
    original_urlopen = credential_module.urlopen
    credential_module.urlopen = _make_success_urlopen()
    try:
        assert cred.get_credential_info() == (
            "id-from-metadata", "key-from-metadata", "token-from-metadata")
        assert cred.get_credential() is cred
    finally:
        credential_module.urlopen = original_urlopen


def test_get_role_name_raises_metadata_error_when_unreachable():
    # the metadata endpoint being unreachable is a configuration error the
    # caller can distinguish from "no role yet": it must raise, not return None
    cred = CVMRoleCredential()
    original_urlopen = credential_module.urlopen
    credential_module.urlopen = _make_failing_role_urlopen(
        IOError("connection refused")
    )
    try:
        try:
            cred.get_role_name()
        except TencentCloudSDKException as e:
            assert e.code == "ClientError.MetadataError"
        else:
            raise AssertionError("expected TencentCloudSDKException")
    finally:
        credential_module.urlopen = original_urlopen


def test_get_credential_returns_none_when_metadata_unreachable():
    # the credential provider chain falls back from CVMRole to TKE OIDC by
    # treating get_credential() == None as "this provider does not apply";
    # an unreachable metadata endpoint must keep that contract
    cred = CVMRoleCredential()
    original_urlopen = credential_module.urlopen
    credential_module.urlopen = _make_failing_role_urlopen(
        IOError("connection refused")
    )
    try:
        assert cred.get_credential() is None
        assert cred.get_credential_info() == (None, None, None)
    finally:
        credential_module.urlopen = original_urlopen


def test_provider_chain_falls_back_to_tke_when_metadata_unreachable():
    # DefaultCredentialProvider tries env vars, profile, CVMRole, then TKE
    # OIDC; an unreachable metadata endpoint must not break that order
    calls = []
    tke_credential = object()  # sentinel handed out by the fake TKE provider

    class FakeEnvCredential(object):
        def get_credential(self):
            calls.append("env")
            return None

    class FakeProfileCredential(object):
        def get_credential(self):
            calls.append("profile")
            return None

    class FakeTkeProvider(object):
        def get_credential(self):
            calls.append("tke")
            return tke_credential

    saved = (
        credential_module.urlopen,
        credential_module.EnvironmentVariableCredential,
        credential_module.ProfileCredential,
        credential_module.DefaultTkeOIDCRoleArnProvider,
    )
    credential_module.urlopen = _make_failing_role_urlopen(
        IOError("connection refused")
    )
    credential_module.EnvironmentVariableCredential = FakeEnvCredential
    credential_module.ProfileCredential = FakeProfileCredential
    credential_module.DefaultTkeOIDCRoleArnProvider = FakeTkeProvider
    try:
        provider = credential_module.DefaultCredentialProvider()
        assert provider.get_credentials() is tke_credential
        assert calls == ["env", "profile", "tke"]
    finally:
        (
            credential_module.urlopen,
            credential_module.EnvironmentVariableCredential,
            credential_module.ProfileCredential,
            credential_module.DefaultTkeOIDCRoleArnProvider,
        ) = saved
