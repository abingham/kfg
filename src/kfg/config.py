from functools import singledispatch


class ConfigKeyError(KeyError):
    pass


class Config:
    def __init__(self):
        self._data = {}

    def __getitem__(self, path):
        return _get(path, self._data)

    def __setitem__(self, path, value):
        _set(path, value, self._data)

    def __contains__(self, path):
        try:
            self[path]
            return True
        except ConfigKeyError:
            return False

    def get(self, path, default=None):
        try:
            return self[path]
        except ConfigKeyError:
            return default


@singledispatch
def _get(path, level):
    try:
        for segment in path[:-1]:
            level = level[segment]

        return level[path[-1]]
    except KeyError:
        raise ConfigKeyError(
            'No config entry at path {}'.format(
                path))
    except TypeError:
        # Assumption is this is caused by indexing an un-indexable object.
        # Perhaps an explicit check above would be cleaner.
        raise ConfigKeyError(
            'No config entry at path {}'.format(
                path))


@_get.register(str)
def _(path, level):
    return _get((path,), level)


@singledispatch
def _set(path, value, level):
    for segment in path[:-1]:
        if segment not in level:
            level[segment] = {}
        level = level[segment]
    level[path[-1]] = value


@_set.register(str)
def _(path, value, level):
    _set((path,), value, level)
