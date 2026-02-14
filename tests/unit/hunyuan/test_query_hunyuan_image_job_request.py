import warnings

from tencentcloud.hunyuan.v20230901.models import QueryHunyuanImageJobRequest


def test_query_hunyuan_image_job_request():
    req = QueryHunyuanImageJobRequest()
    req.JobId = 123
    assert req.JobId == 123


def test_query_hunyuan_image_job_deserialize():
    req = QueryHunyuanImageJobRequest()
    params = {"JobId": 123, "test": "test"}
    with warnings.catch_warnings(record=True) as w:
        req._deserialize(params)
        req.JobId = 123
        assert str(w.pop().message) == "test fileds are useless."
