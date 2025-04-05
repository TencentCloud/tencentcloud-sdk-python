import warnings

from tencentcloud.hunyuan.v20230901.models import GetEmbeddingResponse


def test_hunyuan_get_embedding_response():
    resp = GetEmbeddingResponse()
    resp.Data = 1
    assert resp.Data == 1
    resp.Usage = 10
    assert resp.Usage == 10
    resp.RequestId = "123-ss-2-d-r4-f-42"
    assert resp.RequestId == "123-ss-2-d-r4-f-42"


def test_hunyuan_get_embedding_response_deserialize(mocker):
    resp = GetEmbeddingResponse()
    params = {
        "Data": [1, 2, 3],
        "Usage": 10,
        "RequestId": "123-ss-2-d-r4-f-42"
    }
    with mocker.patch('tencentcloud.hunyuan.v20230901.models.EmbeddingData._deserialize', return_value=111), \
            mocker.patch('tencentcloud.hunyuan.v20230901.models.EmbeddingUsage._deserialize', return_value=222), \
            warnings.catch_warnings(record=True) as w:
        resp._deserialize(params)
        assert resp.RequestId == "123-ss-2-d-r4-f-42"
