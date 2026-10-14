import warnings

from tencentcloud.hunyuan.v20230901.models import EmbeddingUsage


def test_hunyuan_embedding_usage():
    embedding = EmbeddingUsage()
    embedding.PromptTokens = 100
    assert embedding.PromptTokens == 100
    embedding.TotalTokens = 1000
    assert embedding.TotalTokens == 1000


def test_hunyuan_embedding_usage_deserialize():
    embedding = EmbeddingUsage()
    params = {
        "PromptTokens": 100,
        "TotalTokens": 1000,
        "test": "test"
    }
    with warnings.catch_warnings(record=True) as w:
        embedding._deserialize(params)
        assert embedding.PromptTokens == 100
        assert embedding.TotalTokens == 1000
        assert str(w.pop().message) == "test fileds are useless."
