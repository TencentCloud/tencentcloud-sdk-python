import pytest

from tencentcloud.common import abstract_client
from tencentcloud.common.exception import TencentCloudSDKException


def test_build_req_inter_skip_sign(mocker):
    options = {'SkipSign': True}
    client = abstract_client.AbstractClient(None, None, None)
    mock_method = mocker.patch.object(client, '_build_req_without_signature')
    client._build_req_inter('action', {'param': 'value'}, 'req_inter', options)
    assert mock_method.called


def test_build_req_inter_tc3_signature(mocker):
    client = abstract_client.AbstractClient(None, None, None)
    mock_method = mocker.patch.object(client, '_build_req_with_tc3_signature')
    client._build_req_inter('action', {'param': 'value'}, 'req_inter')
    assert mock_method.called


def test_build_req_inter_old_signature(mocker):
    client = abstract_client.AbstractClient(None, None, None)
    client.profile.signMethod = "HmacSHA1"
    mock_method = mocker.patch.object(client, '_build_req_with_old_signature')
    client._build_req_inter('action', {'param': 'value'}, 'req_inter')
    assert mock_method.called


def test_build_req_inter_invalid_signature_method():
    client = abstract_client.AbstractClient(None, None, None)
    client.profile.signMethod = "InvalidMethod"
    with pytest.raises(TencentCloudSDKException) as context:
        client._build_req_inter('action', {'param': 'value'}, 'req_inter')
    assert context.value.code == "ClientError"
    assert context.value.message == "Invalid signature method."
