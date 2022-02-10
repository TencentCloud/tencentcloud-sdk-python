# -*- coding: utf-8 -*-
import json
import os
from itertools import product
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.iai.v20200303 import iai_client, models


def test_big_package_with_signature_v1():
    for sign_method, req_method in product(["HmacSHA1", "HmacSHA256"], ["GET", "POST"]):
        cred = credential.Credential(
            os.environ.get("TENCENTCLOUD_SECRET_ID"),
            os.environ.get("TENCENTCLOUD_SECRET_KEY"))
        http_profile = HttpProfile()
        http_profile.reqMethod = req_method
        client_profile = ClientProfile()
        client_profile.httpProfile = http_profile
        client_profile.signMethod = sign_method
        client = iai_client.IaiClient(cred, "ap-guangzhou", client_profile)

        req = models.CompareFaceRequest()
        params = {
            "ImageA": "1" * 1024 * 1024 * 4,
            "ImageB": "1" * 1024 * 1024 * 1,
            "UrlA": "https://cloudapi-test-1254240205.cos.ap-nanjing.myqcloud.com/9d1f1393e5fc5ca13032e40e3bf9e882.jpeg",
            "UrlB": "https://cloudapi-test-1254240205.cos.ap-nanjing.myqcloud.com/9d1f1393e5fc5ca13032e40e3bf9e882.jpeg",
        }
        req.from_json_string(json.dumps(params))
        try:
            resp = client.CompareFace(req)
            assert False, 'expect fail but success'
        except TencentCloudSDKException:
            pass


def test_big_package_with_signature_v3_get():
    cred = credential.Credential(
        os.environ.get("TENCENTCLOUD_SECRET_ID"),
        os.environ.get("TENCENTCLOUD_SECRET_KEY"))
    http_profile = HttpProfile()
    http_profile.reqMethod = "GET"
    client_profile = ClientProfile()
    client_profile.httpProfile = http_profile
    client_profile.signMethod = "TC3-HMAC-SHA256"
    client = iai_client.IaiClient(cred, "ap-guangzhou", client_profile)

    req = models.CompareFaceRequest()
    params = {
        "ImageA": "1" * 1024 * 1024 * 4,
        "ImageB": "1" * 1024 * 1024 * 1,
        "UrlA": "https://cloudapi-test-1254240205.cos.ap-nanjing.myqcloud.com/9d1f1393e5fc5ca13032e40e3bf9e882.jpeg",
        "UrlB": "https://cloudapi-test-1254240205.cos.ap-nanjing.myqcloud.com/9d1f1393e5fc5ca13032e40e3bf9e882.jpeg",
    }
    req.from_json_string(json.dumps(params))
    try:
        resp = client.CompareFace(req)
        assert False, "expected fail but success"
    except TencentCloudSDKException:
        pass


def test_big_package_with_signature_v3_post():
    cred = credential.Credential(
        os.environ.get("TENCENTCLOUD_SECRET_ID"),
        os.environ.get("TENCENTCLOUD_SECRET_KEY"))
    http_profile = HttpProfile()
    http_profile.reqMethod = "POST"
    client_profile = ClientProfile()
    client_profile.httpProfile = http_profile
    client_profile.signMethod = "TC3-HMAC-SHA256"
    client = iai_client.IaiClient(cred, "ap-guangzhou", client_profile)

    req = models.CompareFaceRequest()
    params = {
        "ImageA": "1" * 1024 * 1024 * 4,
        "ImageB": "1" * 1024 * 1024 * 1,
        "UrlA": "https://cloudapi-test-1254240205.cos.ap-nanjing.myqcloud.com/9d1f1393e5fc5ca13032e40e3bf9e882.jpeg",
        "UrlB": "https://cloudapi-test-1254240205.cos.ap-nanjing.myqcloud.com/9d1f1393e5fc5ca13032e40e3bf9e882.jpeg",
    }
    req.from_json_string(json.dumps(params))
    try:
        resp = client.CompareFace(req)
    except TencentCloudSDKException as e:
        assert e.code in ["FailedOperation.ImageDownloadError"]
