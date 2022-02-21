#!/usr/bin/env python

import os
import site
import sys

from setuptools import setup

if "install" in sys.argv:
    os.system('rm -rf en')
    os.system('mv ru/* .')
    print(os.path.abspath('.'))
    print('okalash {}'.format(os.path.abspath('.')))

setup()


#/home/docs/checkouts/readthedocs.org/user_builds/bona-fide-guru/envs/html/bin/python -m sphinx -T -E -b html -d _build/doctrees -D language=ru . _build/html
