# -*- coding: utf-8 -*-
import json

from tencentcloud.cvm.v20170312 import cvm_client, models


def test_serialization():
    mocked = {
        "InstanceSet": [
            {
                "RenewFlag": "flag_demo",
                "Uuid": "88888888",
                "InstanceState": "RUNNING",
                "LatestOperationState": "SUCCESS",
                "LoginSettings": {
                    "KeyIds": ["skey-*****"],
                    "Password": None,
                    "KeepImageLogin": None
                },
                "IPv6Addresses": None,
                "RestrictState": "NORMAL",
                "ExpiredTime": "2021-07-03T06:30:28Z",
                "Memory": 4,
                "CreatedTime": "2017-07-03T06:30:25Z",
                "CPU": 2,
                "PublicIpAddresses": [
                    "000.000.000.000"
                ],
                "Tags": [],
                "InstanceId": "ins-8888888",
                "ImageId": "img-8888888",
                "StopChargingMode": "NOT_APPLICABLE",
                "InstanceChargeType": "PREPAID",
                "DataDisks": [
                    {
                        "DeleteWithInstance": None,
                        "Encrypt": None,
                        "DiskType": "CLOUD_BASIC",
                        "KmsKeyId": None,
                        "DiskSize": 10,
                        "SnapshotId": None,
                        "DiskId": "disk-8888888",
                        "CdcId": None,
                        "ThroughputPerformance": None,
                    }
                ],
                "InstanceType": "S2.MEDIUM4",
                "SystemDisk": {
                    "DiskSize": 50,
                    "DiskId": "disk-8888888",
                    "DiskType": "CLOUD_BASIC",
                    "CdcId": None
                },
                "Placement": {
                    "HostIds": None,
                    "ProjectId": 0,
                    "HostId": None,
                    "Zone": "ap-shanghai-2",
                    "HostIps": None
                },
                "PrivateIpAddresses": [
                    "000.000.000.000"
                ],
                "OsName": "Ubuntu Server 16.04.1 LTS 64bit",
                "SecurityGroupIds": [
                    "sg-8888888"
                ],
                "CamRoleName": None,
                "InstanceName": "Redis",
                "DisasterRecoverGroupId": "",
                "VirtualPrivateCloud": {
                    "SubnetId": None,
                    "AsVpcGateway": False,
                    "Ipv6AddressCount": None,
                    "VpcId": None,
                    "PrivateIpAddresses": None
                },
                "LatestOperationRequestId": "0b9e9d12-7adb-414b-ae84-8888888",
                "InternetAccessible": {
                    "PublicIpAssigned": None,
                    "InternetChargeType": "BANDWIDTH_PREPAID",
                    "BandwidthPackageId": None,
                    "InternetMaxBandwidthOut": 1
                },
                "LatestOperation": "FailoverMigrateInstance",
                "HpcClusterId": None,
                "RdmaIpAddresses": None,
                "IsolatedSource": None,
            }
        ],
        "TotalCount": 1,
        "RequestId": "46fc254d-c862-401b-a2a0-8888888"
    }
    mocked_json = json.dumps(mocked)
    res = models.DescribeInstancesResponse()
    res.from_json_string(mocked_json)

    actual = json.loads(res.to_json_string())
    for key in actual["InstanceSet"][0]:
        assert actual["InstanceSet"][0][key] == mocked["InstanceSet"][0][key], key
    for key in mocked["InstanceSet"][0]:
        assert actual["InstanceSet"][0][key] == mocked["InstanceSet"][0][key], key
    assert actual == mocked
