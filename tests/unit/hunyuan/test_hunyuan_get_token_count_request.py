import warnings

from tencentcloud.hunyuan.v20230901.models import GetTokenCountRequest


def test_hunyuan_get_token_count_request():
    req = GetTokenCountRequest()
    req.Prompt = 1
    assert req.Prompt == 1


def test_hunyuan_get_token_count_request_deserialize():
    req = GetTokenCountRequest()
    params = {"Prompt": 1, "test": "test"}
    with warnings.catch_warnings(record=True) as w:
        req._deserialize(params)
        assert req.Prompt == 1
        assert str(w.pop().message) == "test fileds are useless."
