"""
Settings used for all tests

Loaded by setup.py
"""
DATABASE = {
    "ENGINE": "django.db.backends.sqlite3",
    "NAME": ":memory:",
}

test_settings = {
    "INSTALLED_APPS": [],
    "DATABASES": {"default": DATABASE, "test": DATABASE},
    # Variables for testing
    "SET_ATTRIBUTE": "test",
    "SET_PROPERTY": "test",
    "SET_CALLABLE": "test",
    "PREFIX_SET_ATTRIBUTE": "prefixed test",
    "PREFIX_SET_PROPERTY": "prefixed test",
    "PREFIX_SET_CALLABLE": "prefixed test",
}
