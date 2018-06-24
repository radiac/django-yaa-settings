import os
import sys
from setuptools import setup, find_packages

VERSION = "1.0.0"

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


def runtests(args):
    "Run tests"
    import django
    from django.conf import settings
    from django.core.management import execute_from_command_line


    if not settings.configured:
        # Configure with settings for tests
        from tests.settings import test_settings
        settings.configure(**test_settings)

    execute_from_command_line(args[:1] + ['test'] + (args[2:] or ['tests']))


if len(sys.argv) > 1 and sys.argv[1] == 'test':
    runtests(sys.argv)
    sys.exit()


setup(
    name = "django-yaa-settings",
    version = VERSION,
    author = "Richard Terry",
    author_email = "code@radiac.net",
    description = ("Yet Another App Settings for Django"),
    license = "BSD",
    url = "http://radiac.net/projects/django-yaa-settings/",
    long_description=read('README.rst'),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        "License :: OSI Approved :: BSD License",
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Framework :: Django',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0',
    ],
    extras_require={
        'dev': ['tox'],
    },
    zip_safe=True,
    packages=find_packages(exclude=('docs', 'tests*',)),
    include_package_data=True,
)
