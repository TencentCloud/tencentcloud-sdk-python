import warnings

from tencentcloud.hunyuan.v20230901.models import GetEmbeddingRequest


def test_hunyuan_get_embedding_request():
    req = GetEmbeddingRequest()
    req.Input = "test_input"
    assert req.Input == "test_input"


def test_hunyuan_get_embedding_request_deserialize():
    req = GetEmbeddingRequest()
    params = {
        "Input": "test_input",
        "test": "test"
    }
    with warnings.catch_warnings(record=True) as w:
        req._deserialize(params)
        assert req.Input == "test_input"
        assert str(w.pop().message) == "test fileds are useless."
