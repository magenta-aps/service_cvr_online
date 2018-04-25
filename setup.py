#
# Copyright (c) 2017, Magenta ApS
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#

from setuptools import setup
from setuptools import find_packages

setup(
    name='service_cvr_online',
    version='0.1',
    description='Lookup information about danish CVR entities',
    author='Steffen Park',
    author_email='steffen@magenta.dk',
    license="MPL 2.0",
    packages=find_packages(),
    package_data={
        '': ["*.txt", "*.xml"]
    },
    zip_safe=False,
    install_requires=[
        "requests==2.18.4",
        "zeep==2.4.0"
    ]
)
