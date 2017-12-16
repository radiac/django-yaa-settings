import os
from setuptools import setup, find_packages

VERSION = "0.0.1"

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "yaa_settings",
    version = VERSION,
    author = "Richard Terry",
    author_email = "code@radiac.net",
    description = ("Yet Another App Settings for Django"),
    license = "BSD",
    url = "http://radiac.net/projects/yaa_settings/",
    long_description=read('README.rst'),
    classifiers=[
        'Development Status :: 4 - Beta',
        #'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        "License :: OSI Approved :: BSD License",
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Framework :: Django',
    ],
    zip_safe=True,
    packages=find_packages(exclude=('docs', 'tests*',)),
    include_package_data=True,
)
