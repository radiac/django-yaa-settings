===================
Django Yaa-Settings
===================

Yet Another App Settings - manage settings for your reusable app

* Project site: http://radiac.net/projects/django-yaa-settings/
* Source code: https://github.com/radiac/django-yaa-settings

.. image:: https://travis-ci.org/radiac/django-yaa-settings.svg?branch=master
    :target: https://travis-ci.org/radiac/django-yaa-settings

.. image:: https://coveralls.io/repos/github/radiac/django-yaa-settings/badge.svg?branch=master
    :target: https://coveralls.io/github/radiac/django-yaa-settings?branch=master


Features
========

* Easy to install and use
* Provide defaults and validate user settings before use
* Works with Django's settings overrides in tests


Version 1.0.0; supports Django 1.8, 1.11 and 2.0 on Python 2.7 and 3.4 upwards.


Installation
============

Install from pip::

    pip install django-yaa-settings


Usage
=====

In your app, create a local ``app_settings.py``::

    from yaa_settings import AppSettings

    class MySettings(AppSettings):
        prefix = 'MYAPP'

        # Can be overridden in Django settings as MYAPP_ATTRIBUTE
        ATTRIBUTE = 'a static value defined at class creation'

        @property
        def PROPERTY(self):
            """
            Return a value calculated whenever it is accessed

            Can be overridden in Django settings as MYAPP_PROPERTY
            """
            return 'a value calculated when accessed'

        def CALLABLE(self, value):
            """
            Always called, passed the MYAPP_CALLABLE value from Django settings
            (or passed None if that is not defined)
            """
            if value is None:
                raise ValueError('MYAPP_CALLABLE must be configured')
            return value


* Import and subclass ``AppSettings``
* Only define one ``AppSettings`` subclass per file
* Set the ``prefix`` attribute if you want to give your settings a prefix in
  Django's settings.
* Settings should be uppercase for consistency with main Django settings.


Now you can access your app's settings directly on the class, without the
prefix::

    from . import app_settings

    def some_method(request):
        if app_settings.ATTRIBUTE == 1:
            return app_settings.PROPERTY
        return app_settings.CALLABLE


You can override these settings in your main Django settings, using the
prefix::

    MYAPP_ATTRIBUTE = 'value available as app_settings.ATTRIBUTE'
    MYAPP_PROPERTY = 'value available as app_settings.PROPERTY'
    MYAPP_CALLABLE = 'value passed to MySettings.CALLABLE'


Why?
====

Use the ``prefix`` to namespace your settings
---------------------------------------------

It's always a good idea to namespace your settings based on your app's name to
avoid collisions with other apps. By using the ``prefix`` attribute you can
omit the prefix throughout your app, making your code neater.

The prefix is optional and you can manually namespace your settings if you'd
prefer the consistency of using the same full setting throughout your project.


Namespace settings while retaining test support
-----------------------------------------------

Using the ``prefix`` mimicks the simpler ``settings.py`` that you find in some
projects::

    from django.conf import settings
    SETTING = getattr(settings, 'MYAPP_SETTINGS', 'default')

but unlike that simpler pattern, Yaa-Settings still works with standard setting
overrides for tests - see the
`Django documentation <https://docs.djangoproject.com/en/2.0/topics/testing/tools/#overriding-settings>`_
for more details.


Create dynamic defaults using properties
----------------------------------------

A property on your ``AppSettings`` subclass will be evaluated every time you
access it, unless you override it in Django's settings. This allows you to
generate dynamic defaults at runtime.



Validate or standardise settings using methods
----------------------------------------------

A method on your ``AppSettings`` subclass will be called every time you access
it, and will be passed the value you have defined in Django's settings. This
allows you to validate settings, or process them ready for use.


Changelog
=========

* 1.0.0, 2018-06-24: Released as stable
* 0.1.0, 2018-06-24: Initial release
