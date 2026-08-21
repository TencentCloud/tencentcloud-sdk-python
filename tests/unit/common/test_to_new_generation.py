from tencentcloud.common.circuit_breaker import CircuitBreaker


class BreakerSetting:
    def __init__(self, window_interval, timeout):
        self.window_interval = window_interval
        self.timeout = timeout


def test_to_new_generation(mocker):
    breaker_setting = BreakerSetting(10, 10)
    cb = CircuitBreaker(breaker_setting)
    cb.state = 0
    cb.to_new_generation(1)
    assert cb.expiry == 11
    cb.state = 2
    cb.to_new_generation(1)
    assert cb.expiry == 11
    cb.state = 1
    with mocker.patch('time.time', return_value=1234567):
        cb.to_new_generation(1)
        assert cb.expiry == 1234567
