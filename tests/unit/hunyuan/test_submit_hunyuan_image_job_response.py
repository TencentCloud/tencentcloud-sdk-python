from tencentcloud.hunyuan.v20230901.models import SubmitHunyuanImageJobResponse


def test_submit_hunyuan_image_job_response():
    resp = SubmitHunyuanImageJobResponse()
    resp.JobId = "11111"
    assert resp.JobId == "11111"

    resp.RequestId = "22222"
    assert resp.RequestId == "22222"


def test_submit_hunyuan_image_job_response_deserialize():
    resp = SubmitHunyuanImageJobResponse()
    params = {
        "JobId": "11111",
        "RequestId": "992js8-2sss-22222",
    }
    resp._deserialize(params)
    assert resp.JobId == "11111"
    assert resp.RequestId == "992js8-2sss-22222"
