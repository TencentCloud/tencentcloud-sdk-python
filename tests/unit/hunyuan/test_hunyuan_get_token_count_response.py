from tencentcloud.hunyuan.v20230901.models import GetTokenCountResponse


def test_hunyuan_get_token_count_response():
    resp = GetTokenCountResponse()
    resp.TokenCount = 10
    assert resp.TokenCount == 10

    resp.CharacterCount = 100
    assert resp.CharacterCount == 100

    resp.RequestId = "123456"
    assert resp.RequestId == "123456"

    resp.Tokens = "1m2ks29sk2www"
    assert resp.Tokens == "1m2ks29sk2www"


def test_hunyuan_get_token_count_response_deserialize():
    resp = GetTokenCountResponse()
    params = {
        "TokenCount": 10,
        "CharacterCount": 100,
        "RequestId": "123456",
        "Tokens": "1m2ks29sk2www"
    }
    resp._deserialize(params)
    assert resp.TokenCount == 10
    assert resp.CharacterCount == 100
    assert resp.RequestId == "123456"
    assert resp.Tokens == "1m2ks29sk2www"
