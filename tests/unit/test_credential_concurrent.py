# -*- coding: utf-8 -*-
import threading
import time
import json
import os
import tempfile
import sys

from tencentcloud.common.credential import *
import tencentcloud.common.credential


class my_patch(object):
    def __init__(self, module, func_name, new_func):
        self.module = module
        self.func_name = func_name
        self.new_func = new_func
        self.original = None

    def __enter__(self):
        self.original = getattr(self.module, self.func_name)
        setattr(self.module, self.func_name, self.new_func)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        setattr(self.module, self.func_name, self.original)


def test_cvm_role_credential_concurrent():
    refresh_counter = [0]
    current_credential = [{"id": "0", "expire_at": 0}]
    inconsistencies = [0]
    refresh_lock = threading.Lock()
    inconsistencies_lock = threading.Lock()
    stop_event = threading.Event()

    def fake_urlopen(url, *args, **kwargs):
        if url.endswith("/cam/security-credentials/"):
            class Resp:
                def read(self):
                    return b"mock-role"
            return Resp()
        elif url.endswith("/cam/security-credentials/mock-role"):
            now = time.time()
            with refresh_lock:
                if now >= current_credential[0]["expire_at"]:
                    refresh_counter[0] += 1
                    value = str(refresh_counter[0])
                    current_credential[0] = {"id": value, "expire_at": now + 1}
                else:
                    value = current_credential[0]["id"]
            class JsonResp:
                def read(self):
                    d = {
                        "TmpSecretId": value,
                        "TmpSecretKey": value,
                        "Token": value,
                        "ExpiredTime": int(current_credential[0]["expire_at"]),
                        "Code": "Success"
                    }
                    try:
                        return json.dumps(d).encode("utf-8")
                    except TypeError:
                        return json.dumps(d)
            return JsonResp()
        raise Exception("Unexpected URL: {}".format(url))

    def worker(thread_id):
        while not stop_event.isSet():
            sid, skey, token = cred.get_credential_info()
            if sid != skey or skey != token:
                with inconsistencies_lock:
                    inconsistencies[0] += 1
            time.sleep(0.001)

    cred = CVMRoleCredential()
    with my_patch(tencentcloud.common.credential, "urlopen", new_func=fake_urlopen):
        threads = []
        for i in range(10):
            t = threading.Thread(target=worker, args=(i,))
            threads.append(t)
            t.start()
        time.sleep(5)
        stop_event.set()
        for t in threads:
            t.join()
    assert inconsistencies[0] == 0, "CVMRoleCredential inconsistencies: {}".format(inconsistencies[0])


def test_role_arn_credential_concurrent():
    refresh_counter = [0]
    current_credential = [{"id": "0", "expire_at": 0}]
    inconsistencies = [0]
    refresh_lock = threading.Lock()
    inconsistencies_lock = threading.Lock()
    stop_event = threading.Event()

    def fake_call_json(self, action, params, options=None):
        now = time.time()
        with refresh_lock:
            if now >= current_credential[0]["expire_at"]:
                refresh_counter[0] += 1
                value = str(refresh_counter[0])
                current_credential[0] = {"id": value, "expire_at": now + 1}
            else:
                value = current_credential[0]["id"]
        return {
            "Response": {
                "Credentials": {
                    "Token": value,
                    "TmpSecretId": value,
                    "TmpSecretKey": value
                },
                "ExpiredTime": int(current_credential[0]["expire_at"])
            }
        }

    def worker(thread_id):
        while not stop_event.isSet():
            sid, skey, token = cred.get_credential_info()
            if sid != skey or skey != token:
                with inconsistencies_lock:
                    inconsistencies[0] += 1
            time.sleep(0.001)

    cred = STSAssumeRoleCredential(
        secret_id="example#test#123456",
        secret_key="example#test#123456",
        role_arn="test-role-arn",
        role_session_name="test-role-session-name",
        duration_seconds=1
    )
    with my_patch(tencentcloud.common.credential.CommonClient, "call_json", new_func=fake_call_json):
        threads = []
        for i in range(10):
            t = threading.Thread(target=worker, args=(i,))
            threads.append(t)
            t.start()
        time.sleep(5)
        stop_event.set()
        for t in threads:
            t.join()
    assert inconsistencies[0] == 0, "RoleArnCredential inconsistencies: {}".format(inconsistencies[0])


def test_oidc_role_arn_credential_concurrent():
    refresh_counter = [0]
    current_credential = [{"id": "0", "expire_at": 0}]
    inconsistencies = [0]
    refresh_lock = threading.Lock()
    inconsistencies_lock = threading.Lock()
    stop_event = threading.Event()

    def fake_call_json(self, action, params, options=None):
        now = time.time()
        with refresh_lock:
            if now >= current_credential[0]["expire_at"]:
                refresh_counter[0] += 1
                value = str(refresh_counter[0])
                current_credential[0] = {"id": value, "expire_at": now + 1}
            else:
                value = current_credential[0]["id"]
        return {
            "Response": {
                "Credentials": {
                    "Token": value,
                    "TmpSecretId": value,
                    "TmpSecretKey": value
                },
                "ExpiredTime": int(current_credential[0]["expire_at"])
            }
        }

    def worker(thread_id):
        while not stop_event.isSet():
            sid, skey, token = cred.get_credential_info()
            if sid != skey or skey != token:
                with inconsistencies_lock:
                    inconsistencies[0] += 1
            time.sleep(0.001)

    cred = OIDCRoleArnCredential(
        region="test-region",
        provider_id="test-provider-id",
        web_identity_token="test-web-identity-token",
        role_arn="test-role-arn",
        role_session_name="test-role-session-name",
        duration_seconds=1
    )

    with my_patch(tencentcloud.common.credential.CommonClient, "call_json", new_func=fake_call_json):
        threads = []
        for i in range(10):
            t = threading.Thread(target=worker, args=(i,))
            threads.append(t)
            t.start()
        time.sleep(5)
        stop_event.set()
        for t in threads:
            t.join()
    assert inconsistencies[0] == 0, "OIDCRoleArnCredential inconsistencies: {}".format(inconsistencies[0])


def test_tke_oidc_role_arn_credential_concurrent():
    refresh_counter = [0]
    current_credential = [{"id": "0", "expire_at": 0}]
    inconsistencies = [0]
    refresh_lock = threading.Lock()
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
        now = time.time()
        with refresh_lock:
            if now >= current_credential[0]["expire_at"]:
                refresh_counter[0] += 1
                value = str(refresh_counter[0])
                current_credential[0] = {"id": value, "expire_at": now + 1}
            else:
                value = current_credential[0]["id"]
        return {
            "Response": {
                "Credentials": {
                    "Token": value,
                    "TmpSecretId": value,
                    "TmpSecretKey": value
                },
                "ExpiredTime": int(current_credential[0]["expire_at"])
            }
        }

    def worker(thread_id):
        while not stop_event.isSet():
            sid, skey, token = cred.get_credential_info()
            if sid != skey or skey != token:
                with inconsistencies_lock:
                    inconsistencies[0] += 1
            time.sleep(0.001)

    cred = DefaultTkeOIDCRoleArnProvider().get_credential()
    with my_patch(tencentcloud.common.credential.CommonClient, "call_json", new_func=fake_call_json):
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
    assert inconsistencies[0] == 0, "TkeOIDCRoleArnProvider inconsistencies: {}".format(inconsistencies[0])
