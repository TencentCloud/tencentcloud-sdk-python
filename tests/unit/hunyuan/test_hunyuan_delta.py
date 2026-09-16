import warnings

from tencentcloud.hunyuan.v20230901.models import Delta, Tool


def test_hunyuan_delta():
    delta = Delta()

    delta.Role = 'normal_user'
    assert delta.Role == 'normal_user'

    delta.Content = 'hello world'
    assert delta.Content == 'hello world'

    delta.ToolCalls = "tool test"
    assert delta.ToolCalls == "tool test"


def test_hunyuan_delta_deserialize(mocker):
    delta = Delta()
    params = {'Role': 'normal_user', 'Content': 'hello world', 'ToolCalls': [1, 2, 3], "test": "test"}
    with mocker.patch('tencentcloud.hunyuan.v20230901.models.ToolCall._deserialize', return_value=111), \
            warnings.catch_warnings(record=True) as captured_warnings:
        delta._deserialize(params)
        assert delta.Role == 'normal_user'
        assert delta.Content == 'hello world'
        assert str(captured_warnings.pop().message) == "test fileds are useless."
