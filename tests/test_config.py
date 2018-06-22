from kfg.config import ConfigKeyError
import pytest


def test_basic_get(config):
    config['foo']['bar'].set(1234)
    assert config['foo']['bar'].get() == 1234


def test_get_missing_key_raises_ConfigKeyError(config):
    with pytest.raises(ConfigKeyError):
        config['foo'].get()


def test_get_invalid_key_access_raises_ConfigKeyError(config):
    config['foo'].set(1)
    with pytest.raises(ConfigKeyError):
        config['foo']['bar'].get()


def test_indexing_into_config_items_works(config):
    config['foo'].set([{'a': 'b'}])
    assert config['foo'][0]['a'].get() == 'b'
