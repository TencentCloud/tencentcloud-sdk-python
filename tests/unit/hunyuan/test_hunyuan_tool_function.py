import warnings

from tencentcloud.hunyuan.v20230901.models import ToolFunction


def test_hunyuan_tool_function():
    function = ToolFunction()
    function.Name = 'Test'
    assert function.Name == 'Test'

    function.Parameters = ["a", "b"]
    assert function.Parameters == ["a", "b"]

    function.Description = 'this is a test'
    assert function.Description == 'this is a test'


def test_hunyuan_tool_function_deserialize():
    function = ToolFunction()
    params = {
        "Name": "test",
        "Description": "this is a test",
        "Parameters": ["a", "b"],
        "test": "test"
    }
    with warnings.catch_warnings(record=True) as w:
        function._deserialize(params)
        assert function.Name == "test"
        assert function.Description == "this is a test"
        assert str(w.pop().message) == "test fileds are useless."
