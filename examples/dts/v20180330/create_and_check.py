# -*- coding: utf-8 -*-
import os
import time

from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.dts.v20180330 import dts_client, models


def NewClient(region):
    cred = credential.Credential(
        os.environ.get("TENCENTCLOUD_SECRET_ID"),
        os.environ.get("TENCENTCLOUD_SECRET_KEY"))

    httpProfile = HttpProfile()
    httpProfile.endpoint = "dts.tencentcloudapi.com"

    clientProfile = ClientProfile()
    clientProfile.httpProfile = httpProfile
    client = dts_client.DtsClient(cred, region, clientProfile)
    return client


def DTSCreateMigrateJob(client, dstId, dstRegion):
    try:
        req = models.CreateMigrateJobRequest()
        params = '''{
            "Region" : "ap-guangzhou",
            "JobName" : "test_0001",
            "MigrateOption" : {"RunMode":1,"MigrateType":2,"MigrateObject":2,"ConsistencyType":5,"IsOverrideRoot":0},
            "SrcDatabaseType" : "mysql",
            "SrcAccessType" : "extranet",
            "SrcInfo" : {
                            "Ip":"151.230.187.23", 
                            "Port":"3306",
                            "Region":"ap-shanghai",
                            "Supplier":"others",
                            "User":"root",
                            "Password":"mypassword"
                        },
            "DstDatabaseType" : "mysql", 
            "DstAccessType" : "cdb",
            "DstInfo" : {
                "InstanceId":"%s",
                "Region":"%s"
                }
        }''' % (dstId, dstRegion)

        req.from_json_string(params)
        req.DatabaseInfo = '[{"Database":"simple","Table":["city"]}]'

        print("DTSCreateMigrateJob with param:\n" + req.to_json_string(sort_keys=True, indent=4))

        resp = client.CreateMigrateJob(req)

        return None, resp
    except TencentCloudSDKException as err:
        return err.code, err


def DTSCreateMigrateCheckJob(client, jobId):
    try:
        req = models.CreateMigrateCheckJobRequest()
        params = '''{
            "JobId": "%s"
        }''' % jobId
        req.from_json_string(params)
        resp = client.CreateMigrateCheckJob(req)
        return None, resp
    except TencentCloudSDKException as err:
        return err.code, err


def DTSDescribeMigrateJobs(client, jobId):
    try:
        req = models.DescribeMigrateJobsRequest()
        params = '''{
            "JobId": "%s"
        }''' % jobId
        req.from_json_string(params)
        resp = client.DescribeMigrateJobs(req)
        return None, resp
    except TencentCloudSDKException as err:
        return err.code, err


def DTSDescribeMigrateCheckJob(client, jobId):
    try:
        req = models.DescribeMigrateCheckJobRequest()
        params = '''{
                "JobId": "%s"
            }''' % jobId
        req.from_json_string(params)
        resp = client.DescribeMigrateCheckJob(req)
        return None, resp
    except TencentCloudSDKException as err:
        return err.code, err


if __name__ == '__main__':
    dstRegion = "ap-chengdu"
    dstCdbId = 'cdb-m50faox0'
    client = NewClient(dstRegion)

    errcode, ret = DTSCreateMigrateJob(client, dstCdbId, dstRegion)
    if errcode is not None:
        print("ERR:%s" % ret)
        exit(1)

    print("created dts job:" + ret.JobId)
    jobId = ret.JobId
    errcode, ret = DTSCreateMigrateCheckJob(client, jobId)
    if errcode is not None:
        print("ERR:%s" % ret)
        exit(1)
    print("check job:" + jobId)

    time.sleep(10)
    isCheckPass = False
    while True:
        errcode, ret = DTSDescribeMigrateJobs(client, jobId)
        if errcode is not None:
            print("ERR:%s" % ret)
        else:
            job = ret.JobList[0]

            if job.Status == 4:
                print(jobId + " check pass")
                isCheckPass = True
                break
            elif job.Status == 5:
                print(jobId + " check failed")
                isCheckPass = False
                break
        time.sleep(2)

    if not isCheckPass:
        errcode, ret = DTSDescribeMigrateCheckJob(client, jobId)
        print("check result:" + ret.to_json_string())
        exit(1)
