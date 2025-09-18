# -*- coding: utf-8 -*-
import asyncio
import os

from tencentcloud.common import credential, retry_async
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.cvm.v20170312 import cvm_client_async, models


async def main():
    try:
        cred = credential.Credential(
            os.environ.get("TENCENTCLOUD_SECRET_ID"),
            os.environ.get("TENCENTCLOUD_SECRET_KEY"))

        cpf = ClientProfile()
        # 如果使用到了重试功能, 需要引入 retry_async
        cpf.retryer = retry_async.StandardRetryer(max_attempts=3)

        # 需要引入 cvm_client_async
        client = cvm_client_async.CvmClient(cred, "ap-shanghai", cpf)

        req = models.DescribeInstancesRequest()

        resp_filter = models.Filter()
        resp_filter.Name = "zone"
        resp_filter.Values = ["ap-shanghai-1", "ap-shanghai-2"]
        req.Filters = [resp_filter]

        resp = await client.DescribeInstances(req)

        print(resp.to_json_string(indent=2))

    except TencentCloudSDKException as err:
        print(err)


asyncio.run(main())
