from datetime import datetime

from tencentcloud.hunyuan.v20230901.models import ChatCompletionsResponse


def test_chat_completions_response():
    response = ChatCompletionsResponse()

    response.Created = datetime(year=2020, month=1, day=1)
    assert response.Created == datetime(year=2020, month=1, day=1)

    response.Usage = 10
    assert response.Usage == 10

    response.Note = "test"
    assert response.Note == "test"

    response.Id = 123456
    assert response.Id == 123456

    response.Choices = 1
    assert response.Choices == 1

    response.RequestId = 'a-dm338d-s3ms3k4s-sa'
    assert response.RequestId == 'a-dm338d-s3ms3k4s-sa'

    response.ErrorMsg = "test"
    assert response.ErrorMsg == "test"


def test_chat_completions_response_deserialize(mocker):
    response = ChatCompletionsResponse()
    params = {
        "Created": "2020-01-01",
        "Usage": 10,
        "Note": "test",
        "Id": 123456,
        "Choices": [1, 2, 3],
        "RequestId": "a-dm338d-s3ms3k4s-sa",
        "ErrorMsg": "test"
    }
    with mocker.patch('tencentcloud.hunyuan.v20230901.models.Usage._deserialize', return_value=111) as mock_usage, \
            mocker.patch('tencentcloud.hunyuan.v20230901.models.Choice._deserialize', return_value=222) as mock_Choice, \
            mocker.patch('tencentcloud.hunyuan.v20230901.models.ErrorMsg._deserialize',
                         return_value=333) as mock_ErrorMsg:
        response._deserialize(params)
        assert response._Created == "2020-01-01"
