from kfg.config import ConfigKeyError
import pytest


def test_set_followed_by_get_results_in_correct_value(config, key):
    config[key] = 1234
    assert config[key] == 1234


def test_get_missing_key_raises_ConfigKeyError(config, key):
    with pytest.raises(ConfigKeyError):
        config[key]


def test_get_invalid_key_access_raises_ConfigKeyError(config, key):
    config[key] = 1
    bad_key = (key, 'oops')
    with pytest.raises(ConfigKeyError):
        config[bad_key]


def test_indexing_into_config_items_works(config):
    config['foo'] = [{'a': 'b'}]
    assert config['foo', 0, 'a'] == 'b'


def test_get_missing_key_with_default_returns_default(config, key):
    assert config.get(key, 42) == 42
    assert config.get(key, default=42) == 42


def test_contains_returns_true_for_existing_value(config, key):
    config[key] = 1234
    assert key in config


def test_contains_returns_false_for_non_existing_value(config, key):
    assert (key, 'oops') not in config
