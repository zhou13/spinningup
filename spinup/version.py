version_info = (0, 2, 0)


def get_version():
    "Returns the version as a human-format string."
    return "%d.%d.%d" % version_info


__version__ = get_version()
