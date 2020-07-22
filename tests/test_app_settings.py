"""
Test an AppSettings without a prefix
"""
from django.test import TestCase, override_settings

from . import app_settings_no_prefix, app_settings_with_prefix


class TestAppSettingsWithoutPrefix(TestCase):
    def test_attribute_default(self):
        self.assertEqual(app_settings_no_prefix.UNSET_ATTRIBUTE, "default")

    def test_attribute_overridden_in_settings(self):
        self.assertEqual(app_settings_no_prefix.SET_ATTRIBUTE, "test")

    @override_settings(SET_ATTRIBUTE="overridden")
    def test_attribute_overridden_in_tests(self):
        self.assertEqual(app_settings_no_prefix.SET_ATTRIBUTE, "overridden")

    def test_property_default(self):
        self.assertEqual(app_settings_no_prefix.UNSET_PROPERTY, "default")

    def test_property_overridden(self):
        self.assertEqual(app_settings_no_prefix.SET_PROPERTY, "test")

    @override_settings(SET_PROPERTY="overridden")
    def test_property_overridden_in_tests(self):
        self.assertEqual(app_settings_no_prefix.SET_PROPERTY, "overridden")

    def test_callable_default(self):
        self.assertEqual(app_settings_no_prefix.UNSET_CALLABLE, "unset")

    def test_callable_overridden(self):
        self.assertEqual(app_settings_no_prefix.SET_CALLABLE, "called test")

    @override_settings(SET_CALLABLE="overridden")
    def test_callable_overridden_in_tests(self):
        self.assertEqual(app_settings_no_prefix.SET_CALLABLE, "called overridden")

    def test_undefined(self):
        with self.assertRaises(AttributeError):
            assert app_settings_no_prefix.UNDEFINED


class TestAppSettingsWithPrefix(TestCase):
    def test_attribute_default(self):
        self.assertEqual(app_settings_with_prefix.UNSET_ATTRIBUTE, "default")

    def test_attribute_overridden(self):
        self.assertEqual(app_settings_with_prefix.SET_ATTRIBUTE, "prefixed test")

    @override_settings(PREFIX_SET_ATTRIBUTE="prefixed overridden")
    def test_attribute_overridden_in_tests(self):
        self.assertEqual(app_settings_with_prefix.SET_ATTRIBUTE, "prefixed overridden")

    def test_property_default(self):
        self.assertEqual(app_settings_with_prefix.UNSET_PROPERTY, "default")

    def test_property_overridden(self):
        self.assertEqual(app_settings_with_prefix.SET_PROPERTY, "prefixed test")

    @override_settings(PREFIX_SET_PROPERTY="prefixed overridden")
    def test_property_overridden_in_tests(self):
        self.assertEqual(app_settings_with_prefix.SET_PROPERTY, "prefixed overridden")

    def test_callable_default(self):
        self.assertEqual(app_settings_with_prefix.UNSET_CALLABLE, "unset")

    def test_callable_overridden(self):
        self.assertEqual(app_settings_with_prefix.SET_CALLABLE, "called prefixed test")

    @override_settings(PREFIX_SET_CALLABLE="prefixed overridden")
    def test_callable_overridden_in_tests(self):
        self.assertEqual(
            app_settings_with_prefix.SET_CALLABLE, "called prefixed overridden"
        )

    def test_using_prefix__raises_exception(self):
        with self.assertRaises(AttributeError):
            assert app_settings_with_prefix.PREFIX_SET_ATTRIBUTE

    def test_undefined(self):
        with self.assertRaises(AttributeError):
            assert app_settings_with_prefix.UNDEFINED
