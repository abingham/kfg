from kfg.config import ConfigValueError
import pytest

def test_transform_violation_raises_ConfigValueError(config, key):
    config[key] = 'bar'
    config.set_transform(
        key=key,
        transform=int,
    )
    with pytest.raises(ConfigValueError):
        config[key]
