import warnings

from tencentcloud.hunyuan.v20230901.models import EmbeddingData


def test_hunyuan_embedding_data():
    embedding = EmbeddingData()
    embedding.Embedding = 'test/embedding/embedding'
    assert embedding.Embedding == 'test/embedding/embedding'

    embedding.Index = 'test/embedding/index'
    assert embedding.Index == 'test/embedding/index'

    embedding.Object = True
    assert embedding.Object is True


def test_hunyuan_embedding_data_deserialize():
    embedding = EmbeddingData()
    params = {
        'Embedding': 'test/embedding/embedding',
        'Index': 'test/embedding/index',
        'Object': True,
        "test": "test"
    }
    with warnings.catch_warnings(record=True) as w:
        embedding._deserialize(params)
        assert embedding.Embedding == 'test/embedding/embedding'
        assert embedding.Index == 'test/embedding/index'
        assert embedding.Object is True
        assert str(w.pop().message) == "test fileds are useless."
