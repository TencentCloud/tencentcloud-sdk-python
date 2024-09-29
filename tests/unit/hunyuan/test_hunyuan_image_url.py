import warnings

from tencentcloud.hunyuan.v20230901.models import ImageUrl


def test_hunyuan_image_url():
    image = ImageUrl()
    image.Url = "https://hunyuan.com"
    assert image.Url == "https://hunyuan.com"


def test_hunyuan_image_url_deserialize():
    image = ImageUrl()
    params = {"Url": "https://hunyuan.com", "test": "test"}
    with warnings.catch_warnings(record=True) as w:
        image._deserialize(params)
        assert image.Url == "https://hunyuan.com"
        assert str(w.pop().message) == "test fileds are useless."
