#!/usr/bin/env python
# Copyright (c) 2013 Arista Networks, Inc.  All rights reserved.

# git repo sourced from: https://github.com/aristanetworks/httpbin

import setuptools

setuptools.setup(
   name='httpbin',
   version='0.1',  # git repo commit 180283a60a1d060309eefdca3d769b1ec2d2ddb9
   packages=[ 'httpbin' ],
   package_data={ 'httpbin': [ 'templates/*.html' ] },
)
