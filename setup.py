#!/usr/bin/env python

import os
import site
import sys

from setuptools import setup

if "install" in sys.argv:
    os.system('rm -rf en')
    os.system('mv ru/* .')

setup()


