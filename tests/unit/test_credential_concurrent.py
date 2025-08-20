import threading
import time
import json
import os
import tempfile
import pytest
from unittest.mock import patch, MagicMock
from tencentcloud.common.credential import *


def test_cvm_role_credential_concurrent():
    refresh_counter = 0
    refresh_lock = threading.Lock()
    current_credential = {"id": "0", "expire_at": 0}
    inconsistencies = 0
    inconsistencies_lock = threading.Lock()
    stop_event = threading.Event()

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

    def worker(thread_id):
        nonlocal inconsistencies
        while not stop_event.is_set():
            sid, skey, token = cred.get_credential_info()
            if sid != skey or skey != token:
                with inconsistencies_lock:
                    inconsistencies += 1
                print(f"[Thread {thread_id}] Inconsistent: {sid} / {skey} / {token}", flush=True)
            time.sleep(0.001)

    with patch("tencentcloud.common.credential.urlopen", new=fake_urlopen):
        cred = CVMRoleCredential()
        threads = []
        for i in range(10):
            t = threading.Thread(target=worker, args=(i,))
            threads.append(t)
            t.start()

        time.sleep(5)
        stop_event.set()
        for t in threads:
            t.join()

    assert inconsistencies == 0, f"CVMRoleCredential inconsistencies: {inconsistencies}"


def test_role_arn_credential_concurrent():
    refresh_counter = 0
    refresh_lock = threading.Lock()
    current_credential = {"id": "0", "expire_at": 0}
    inconsistencies = 0
    inconsistencies_lock = threading.Lock()
    stop_event = threading.Event()

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

    def worker(thread_id):
        nonlocal inconsistencies
        while not stop_event.is_set():
            sid, skey, token = cred.get_credential_info()
            if sid != skey or skey != token:
                with inconsistencies_lock:
                    inconsistencies += 1
                print(f"[Thread {thread_id}] Inconsistent: {sid} / {skey} / {token}", flush=True)
            time.sleep(0.001)

    cred = STSAssumeRoleCredential(
        secret_id = "test-secret-id",
        secret_key= "test-secret-key",
        role_arn="test-role-arn",
        role_session_name="test-role-session-name",
        duration_seconds=1
    )

    with patch("tencentcloud.common.credential.CommonClient.call_json", new=fake_call_json):
        threads = []
        for i in range(10):
            t = threading.Thread(target=worker, args=(i,))
            threads.append(t)
            t.start()

        time.sleep(5)
        stop_event.set()
        for t in threads:
            t.join()

    assert inconsistencies == 0, f"RoleArnCredential inconsistencies: {inconsistencies}"


def test_oidc_role_arn_credential_concurrent():
    refresh_counter = 0
    refresh_lock = threading.Lock()
    current_credential = {"id": "0", "expire_at": 0}
    inconsistencies = 0
    inconsistencies_lock = threading.Lock()
    stop_event = threading.Event()

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

    def worker(thread_id):
        nonlocal inconsistencies
        while not stop_event.is_set():
            sid, skey, token = cred.get_credential_info()
            if sid != skey or skey != token:
                with inconsistencies_lock:
                    inconsistencies += 1
                print(f"[Thread {thread_id}] Inconsistent: {sid} / {skey} / {token}", flush=True)
            time.sleep(0.001)


    cred = OIDCRoleArnCredential(
        region="test-region",
        provider_id="test-provider-id",
        web_identity_token="test-web-identity-token",
        role_arn="test-role-arn",
        role_session_name="test-role-session-name",
        duration_seconds=1
    )

    with patch("tencentcloud.common.credential.CommonClient.call_json", new=fake_call_json):
        threads = []
        for i in range(10):
            t = threading.Thread(target=worker, args=(i,))
            threads.append(t)
            t.start()

        time.sleep(5)
        stop_event.set()
        for t in threads:
            t.join()

    assert inconsistencies == 0, f"OIDCRoleArnCredential inconsistencies: {inconsistencies}"



def test_tke_oidc_role_arn_credential_concurrent():
    refresh_counter = 0
    refresh_lock = threading.Lock()
    current_credential = {"id": "0", "expire_at": 0}
    inconsistencies = 0
    inconsistencies_lock = threading.Lock()
    stop_event = threading.Event()

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

    def worker(thread_id):
        nonlocal inconsistencies
        while not stop_event.is_set():
            sid, skey, token = cred.get_credential_info()
            if sid != skey or skey != token:
                with inconsistencies_lock:
                    inconsistencies += 1
                print(f"[Thread {thread_id}] Inconsistent: {sid} / {skey} / {token}", flush=True)
            time.sleep(0.001)

    cred = DefaultTkeOIDCRoleArnProvider().get_credential()

    with patch("tencentcloud.common.credential.CommonClient.call_json", new=fake_call_json):
        threads = []
        for i in range(10):
            t = threading.Thread(target=worker, args=(i,))
            threads.append(t)
            t.start()

        time.sleep(5)
        stop_event.set()
        for t in threads:
            t.join()

    os.remove(token_file)

    assert inconsistencies == 0, f"TkeOIDCRoleArnProvider inconsistencies: {inconsistencies}"