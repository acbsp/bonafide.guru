#!/usr/bin/env python

import os
import site
import sys

from setuptools import setup

if "install" in sys.argv:

    print('okalash SETUP ======================================')
    print('okalash SETUP {}'.format(os.path.abspath('.')))
    os.system('cp -a _static ru/')
    os.system('cp -a _extra ru/')
    os.system('cp -a fonts ru/')
    os.system('cp -a images ru/')
    os.system('ls -la ru/*')
    print('okalash SETUP ======================================')

    os.system('rm -rf en')
    #os.system('mv ru/* .')
    #print('okalash 0 {}'.format(os.path.abspath('.')))
    os.system('bash ru/pre.sh html ru')
    #print('okalash 1 {}'.format(os.path.abspath('.')))
    #os.system('bash pre.sh')
    #print('okalash 2 {}'.format(os.path.abspath('.')))

setup()


#/home/docs/checkouts/readthedocs.org/user_builds/bona-fide-guru/envs/html/bin/python -m sphinx -T -E -b html -d _build/doctrees -D language=ru . _build/html

#/home/docs/checkouts/readthedocs.org/user_builds/bona-fide-guru/checkouts/html/ru
