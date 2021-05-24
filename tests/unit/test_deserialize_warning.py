# -*- coding: utf-8 -*-
import warnings

from tencentcloud.cvm.v20170312 import models

try:
    warnings.simplefilter('error')
    req = models.DescribeInstancesRequest()

    params = '''{
        "Filters": [
            {
                "Name": "zone",
                "Values": ["ap-shanghai-1", "ap-shanghai-2"],
                "a": "a"

            }
        ]
    }'''
    req.from_json_string(params)

except Exception as err:
    assert "fileds are useless" in str(err)
