# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "simple_item_manager"
VERSION = "1.0.0"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "connexion>=2.0.2",
    "swagger-ui-bundle>=0.0.2",
    "python_dateutil>=2.6.0"
]

setup(
    name=NAME,
    version=VERSION,
    description="簡易物品管理WebAPI",
    author_email="",
    url="",
    keywords=["OpenAPI", "簡易物品管理WebAPI"],
    install_requires=REQUIRES,
    extras_require={
        "dev": ["sqlacodegen"]
    },
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['simple_item_manager=simple_item_manager.__main__:main']},
    long_description="""\
    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
    """
)

