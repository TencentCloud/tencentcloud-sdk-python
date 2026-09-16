import warnings

from tencentcloud.hunyuan.v20230901.models import ToolCall


def test_hunyuan_tool_call():
    call = ToolCall()
    call.Type = 'test'
    assert call.Type == 'test'

    call.Id = '123456'
    assert call.Id == '123456'

    call.Function = 'mock_function'
    assert call.Function == 'mock_function'


def test_hunyuan_tool_call_deserialize(mocker):
    call = ToolCall()
    params = {
        'Type': 'test',
        'Id': '123456',
        'Function': 'mock_function',
        'test': 'test'
    }
    with mocker.patch('tencentcloud.hunyuan.v20230901.models.ToolCallFunction._deserialize', return_value=111), \
            warnings.catch_warnings(record=True) as w:
        call._deserialize(params)
        assert call.Type == 'test'
        assert str(w.pop().message) == "test fileds are useless."
