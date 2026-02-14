import os


from tencentcloud.common import abstract_client, credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile


def test_normal_request(mocker):
    cred = credential.Credential(
        os.environ.get("TENCENTCLOUD_SECRET_ID"),
        os.environ.get("TENCENTCLOUD_SECRET_KEY"))
    httpProfile = HttpProfile()
    httpProfile.endpoint = "sts.tencentcloudapi.com"

    clientProfile = ClientProfile()
    clientProfile.httpProfile = httpProfile
    clientProfile.signMethod = "HmacSHA256"
    clientProfile.disable_region_breaker = False

    client = abstract_client.AbstractClient(cred, None, profile=clientProfile)
    action = "DescribeServices"
    params = {"service": "cvm"}
    mock_request = mocker.patch.object(client, 'request')
    client._call_with_region_breaker(action, params)
    mock_request.send_request.assert_called_once()


def test_circuit_breaker_open(mocker):
    cred = credential.Credential(
        os.environ.get("TENCENTCLOUD_SECRET_ID"),
        os.environ.get("TENCENTCLOUD_SECRET_KEY"))
    httpProfile = HttpProfile()
    httpProfile.endpoint = "sts.tencentcloudapi.com"

    clientProfile = ClientProfile()
    clientProfile.httpProfile = httpProfile
    clientProfile.signMethod = "HmacSHA256"
    clientProfile.disable_region_breaker = False

    client = abstract_client.AbstractClient(cred, None, profile=clientProfile)

    action = "DescribeServices"
    params = {"service": "cvm"}
    mocker_circuit_breaker = mocker.patch.object(client, 'circuit_breaker')
    mocker_circuit_breaker.before_requests.return_value = 1, True
    client._call_with_region_breaker(action, params)
    assert ".tencentcloudapi.com" in client._get_endpoint()

