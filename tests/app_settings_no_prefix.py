"""
Sample app settings without a prefix
"""

from yaa_settings import AppSettings


class NoPrefixSettings(AppSettings):
    # A value which is set in settings (see setup.py)
    SET_ATTRIBUTE = "default"

    # A value which is not set in settings
    UNSET_ATTRIBUTE = "default"

    @property
    def SET_PROPERTY(self):
        return "default"

    @property
    def UNSET_PROPERTY(self):
        return "default"

    def SET_CALLABLE(self, value):
        if value is None:
            return "unset"
        return "called {}".format(value)

    def UNSET_CALLABLE(self, value):
        if value is None:
            return "unset"
        return "called {}".format(value)
