import warnings

from tencentcloud.hunyuan.v20230901.models import Content


def test_hunyuan_content():
    content = Content()

    content.Type = 1
    content.Text = "111.text"
    content.ImageUrl = "https://hunyuan.com"
    assert content.Type == 1
    assert content.Text == "111.text"
    assert content.ImageUrl == "https://hunyuan.com"


def test_hunyuan_deserialize(mocker):
    content = Content()
    params = {
        "Type": 1,
        "Text": "111.text",
        "ImageUrl": "https://hunyuan.com",
        "test": "test"
    }
    with mocker.patch('tencentcloud.hunyuan.v20230901.models.ImageUrl._deserialize', return_value=111), \
            warnings.catch_warnings(record=True) as captured_warnings:
        content._deserialize(params)
        assert content._Type == 1
        assert content._Text == "111.text"
        assert str(captured_warnings.pop().message) == "test fileds are useless."
