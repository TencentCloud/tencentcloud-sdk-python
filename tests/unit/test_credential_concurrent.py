import threading
import time
import json
import os
import tempfile
import pytest
from unittest.mock import patch, MagicMock
from tencentcloud.common.credential import *


def run_concurrent_credential_test(cred, num_threads=50, duration=10):
    inconsistencies = 0
    inconsistencies_lock = threading.Lock()
    stop_event = threading.Event()

    def worker(thread_id):
        nonlocal inconsistencies
        while not stop_event.is_set():
            sid, skey, token = cred.get_tmp_credential_info()
            if sid != skey or skey != token:
                with inconsistencies_lock:
                    inconsistencies += 1
                print(f"[Thread {thread_id}] Inconsistent: {sid} / {skey} / {token}", flush=True)
            time.sleep(0.001)

    threads = []
    for i in range(num_threads):
        t = threading.Thread(target=worker, args=(i,))
        threads.append(t)
        t.start()

    time.sleep(duration)
    stop_event.set()
    for t in threads:
        t.join()

    return inconsistencies


def test_cvm_role_credential_concurrent():
    refresh_counter = 0
    refresh_lock = threading.Lock()
    current_credential = {"id": "0", "expire_at": 0}

    def fake_urlopen(url, *args, **kwargs):
        nonlocal refresh_counter, current_credential

        if url.endswith("/cam/security-credentials/"):
            class Resp:
                def read(self):
                    return b"mock-role"
            return Resp()

        elif url.endswith("/cam/security-credentials/mock-role"):
            now = time.time()
            with refresh_lock:
                if now >= current_credential["expire_at"]:
                    refresh_counter += 1
                    value = str(refresh_counter)
                    current_credential = {
                        "id": value,
                        "expire_at": now + 1
                    }
                else:
                    value = current_credential["id"]

            class JsonResp:
                def read(self):
                    return json.dumps({
                        "TmpSecretId": value,
                        "TmpSecretKey": value,
                        "Token": value,
                        "ExpiredTime": int(current_credential["expire_at"]),
                        "Code": "Success"
                    }).encode("utf-8")
            return JsonResp()

        raise Exception(f"Unexpected URL: {url}")

    with patch("tencentcloud.common.credential.urlopen", new=fake_urlopen):
        cred = CVMRoleCredential()
        inconsistencies = run_concurrent_credential_test(cred, num_threads=50, duration=10)

    assert inconsistencies == 0, f"CVMRoleCredential inconsistencies: {inconsistencies}"


def test_role_arn_credential_concurrent():
    refresh_counter = 0
    refresh_lock = threading.Lock()
    current_credential = {"id": "0", "expire_at": 0}

    def fake_call_json(self, action, params, options=None):
        nonlocal refresh_counter, current_credential

        now = time.time()
        with refresh_lock:
            if now >= current_credential["expire_at"]:
                refresh_counter += 1
                value = str(refresh_counter)
                current_credential = {
                    "id": value,
                    "expire_at": now + 1
                }
            else:
                value = current_credential["id"]

        return {
            "Response": {
                "Credentials": {
                    "Token": value,
                    "TmpSecretId": value,
                    "TmpSecretKey": value
                },
                "ExpiredTime": int(current_credential["expire_at"])
            }
        }

    cred = STSAssumeRoleCredential(
        secret_id="mock-secret-id",
        secret_key="mock-secret-key",
        role_arn="mock-role-arn",
        role_session_name="session-1",
        duration_seconds=1
    )

    with patch("tencentcloud.common.credential.CommonClient.call_json", new=fake_call_json):
        inconsistencies = run_concurrent_credential_test(cred, num_threads=100, duration=10)

    assert inconsistencies == 0, f"RoleArnCredential inconsistencies: {inconsistencies}"


def test_oidc_role_arn_credential_concurrent():
    refresh_counter = 0
    refresh_lock = threading.Lock()
    current_credential = {"id": "0", "expire_at": 0}

    def fake_call_json(self, action, params, options=None):
        nonlocal refresh_counter, current_credential

        now = time.time()
        with refresh_lock:
            if now >= current_credential["expire_at"]:
                refresh_counter += 1
                value = str(refresh_counter)
                current_credential = {
                    "id": value,
                    "expire_at": now + 1
                }
            else:
                value = current_credential["id"]

        return {
            "Response": {
                "Credentials": {
                    "Token": value,
                    "TmpSecretId": value,
                    "TmpSecretKey": value
                },
                "ExpiredTime": int(current_credential["expire_at"])
            }
        }

    with patch("tencentcloud.common.credential.CommonClient.call_json", new=fake_call_json):
        cred = OIDCRoleArnCredential(
            region="ap-guangzhou",
            provider_id="mock-provider-id",
            web_identity_token="mock-token",
            role_arn="mock-role-arn",
            role_session_name="session-1",
            duration_seconds=1
        )
        inconsistencies = run_concurrent_credential_test(cred, num_threads=100, duration=10)

    assert inconsistencies == 0, f"OIDCRoleArnCredential inconsistencies: {inconsistencies}"



def test_tke_oidc_role_arn_credential_concurrent():
    refresh_counter = 0
    refresh_lock = threading.Lock()
    current_credential = {"id": "0", "expire_at": 0}

    with tempfile.NamedTemporaryFile(mode="w", delete=False) as f:
        f.write("mock-token")
        token_file = f.name

    os.environ["TKE_REGION"] = "ap-guangzhou"
    os.environ["TKE_PROVIDER_ID"] = "mock-provider-id"
    os.environ["TKE_WEB_IDENTITY_TOKEN_FILE"] = token_file
    os.environ["TKE_ROLE_ARN"] = "mock-role-arn"

    def fake_call_json(self, action, params, options=None):
        nonlocal refresh_counter, current_credential

        now = time.time()
        with refresh_lock:
            if now >= current_credential["expire_at"]:
                refresh_counter += 1
                value = str(refresh_counter)
                current_credential = {
                    "id": value,
                    "expire_at": now + 1
                }
            else:
                value = current_credential["id"]

        return {
            "Response": {
                "Credentials": {
                    "Token": value,
                    "TmpSecretId": value,
                    "TmpSecretKey": value
                },
                "ExpiredTime": int(current_credential["expire_at"])
            }
        }

    with patch("tencentcloud.common.credential.CommonClient.call_json", new=fake_call_json):
        cred = DefaultTkeOIDCRoleArnProvider().get_credential()
        inconsistencies = run_concurrent_credential_test(cred, num_threads=100, duration=10)

    os.remove(token_file)

    assert inconsistencies == 0, f"TkeOIDCRoleArnProvider inconsistencies: {inconsistencies}"