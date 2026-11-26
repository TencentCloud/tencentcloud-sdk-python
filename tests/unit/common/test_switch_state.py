from tencentcloud.common.circuit_breaker import CircuitBreaker


def test_switch_state(mocker):
    breaker_setting = mocker.MagicMock()
    breaker_setting.window_interval.return_value = 10
    cb = CircuitBreaker(breaker_setting)
    assert cb.switch_state(0, 0) is None

    to_new_generation = mocker.patch.object(cb, "to_new_generation")
    cb.switch_state(1,0)
    to_new_generation.assert_called_once()
