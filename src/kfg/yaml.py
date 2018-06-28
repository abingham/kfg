import yaml

from kfg.config import Config


def load_config(stream):
    """Load a configuration from a file-like object.

    Returns: A `Config` instance.

    Raises:
      ValueError: If there is an error loading the config.
    """
    try:
        data = yaml.safe_load(stream)
        config = Config()
        config._data = data
        return config
    except (OSError, UnicodeDecodeError, yaml.parser.ParserError) as exc:
        raise ValueError(
            'Error loading configuration from {}'.format(stream)) from exc


def serialize_config(config):
    """Convert a `Config` into a string.

    This is complementary with `load_config`.
    """
    return yaml.dump(config._data)
