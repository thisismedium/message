### Copyright (c) 2010, Coptix, Inc.  All rights reserved.
### See the LICENSE file for license terms and warranty disclaimer.

"""setup -- create a Message development environment."""

from setuptools import setup, find_packages

setup(
    name = 'message',
    version = '0.3',
    description = 'A versioned datastore for managing structured content.',
    author = 'Medium',
    author_email = 'labs@thisismedium.com',
    url = 'http://messagecms.com/',
    license = 'BSD',
    keywords = 'database datastore key-value versioned web cms content',
    packages = list(find_packages())
)
