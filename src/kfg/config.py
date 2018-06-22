class ConfigKeyError(KeyError):
    pass


class ConfigCursor:
    def __init__(self, config):
        self._config = config
        self._path = []

    def __getitem__(self, name):
        self._path.append(name)
        return self

    def set(self, value):
        level = self._config._data
        for segment in self._path[:-1]:
            if segment not in level:
                level[segment] = {}
            level = level[segment]
        level[self._path[-1]] = value

    def get(self):
        level = self._config._data
        try:
            for segment in self._path[:-1]:
                level = level[segment]

            return level[self._path[-1]]
        except KeyError:
            raise ConfigKeyError(
                'No config entry at path {}'.format(
                    self._path))
        except TypeError:
            # Assumption is this is caused by indexing an un-indexable object.
            # Perhaps an explicit check above would be cleaner.
            raise ConfigKeyError(
                'No config entry at path {}'.format(
                    self._path))


class Config:
    def __init__(self):
        self._data = {}

    def __getitem__(self, name):
        return ConfigCursor(self)[name]
