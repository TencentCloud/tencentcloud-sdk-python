import warnings

from tencentcloud.hunyuan.v20230901.models import Usage


def test_hunyuan_usage():
    usage = Usage()
    usage.TotalTokens = 100
    assert usage.TotalTokens == 100

    usage.PromptTokens = 10
    assert usage.PromptTokens == 10

    usage.CompletionTokens = 9
    assert usage.CompletionTokens == 9


def test_hunyuan_usage_deserialize():
    usage = Usage()
    params = {
        "TotalTokens": 100,
        "PromptTokens": 999,
        "CompletionTokens": 888,
        "test": "test"
    }
    with warnings.catch_warnings(record=True) as w:
        usage._deserialize(params)
        assert usage.TotalTokens == 100
        assert usage.PromptTokens == 999
        assert usage.CompletionTokens == 888
        assert str(w.pop().message) == "test fileds are useless."
