# -*- coding: utf-8 -*-
import warnings

import pytest

from tencentcloud.cvm.v20170312 import models


def test_deserialize_warning():
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

    with pytest.raises(Exception) as e:
        req.from_json_string(params)
    assert "fileds are useless" in str(e)
