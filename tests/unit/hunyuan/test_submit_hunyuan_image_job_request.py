import warnings

from tencentcloud.hunyuan.v20230901.models import SubmitHunyuanImageJobRequest


def test_submit_hunyuan_image_job_request():
    req = SubmitHunyuanImageJobRequest()
    req.Prompt = "test"
    assert req.Prompt == "test"

    req.Style = "code"
    assert req.Style == "code"

    req.Resolution = 1
    assert req.Resolution == 1

    req.LogoAdd = True
    assert req.LogoAdd == True

    req.Revise = "test"
    assert req.Revise == "test"


def test_submit_hunyuan_image_job_request_deserialize():
    req = SubmitHunyuanImageJobRequest()
    params = {
        "Prompt": "test",
        "Style": "code",
        "Resolution": 1,
        "LogoAdd": True,
        "Revise": "test",
        "test": "test",
    }
    with warnings.catch_warnings(record=True) as w:
        req._deserialize(params)
        assert req.Prompt == "test"
        assert str(w.pop().message) == "test fileds are useless."
