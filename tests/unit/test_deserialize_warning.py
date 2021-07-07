# -*- coding: utf-8 -*-
import warnings

import pytest

from tencentcloud.cvm.v20170312 import models


def test_req_deserialize_warning():
    warnings.simplefilter('error')

    req = models.DescribeInstancesRequest()
    params = '''{
        "TopUnknownField": "some value",
        "Filters": [
            {
                "Name": "zone",
                "Values": ["ap-shanghai-1", "ap-shanghai-2"],
                "InnerUnknownField": "some value"
            }
        ]
    }'''

    with pytest.raises(Exception) as e:
        req.from_json_string(params)
    assert "fileds are useless" in str(e)


def test_resp_deserialize_no_warning():
    warnings.simplefilter('error')
    resp = models.DescribeRegionsResponse()
    jsonstr = '''{
        "RegionSet": [{
            "InnerUnknownField": "some value"
        }],
        "TopUnknownField": "some value"
    }'''
    resp.from_json_string(jsonstr)
