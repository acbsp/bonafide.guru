#!/usr/bin/env python

import os
import site
import sys

from setuptools import setup

if "install" in sys.argv:
    print('okalash SETUP ======================================')
    os.system('cp -a _static ru/')
    os.system('cp -a fonts ru/')
    os.system('cp -a images ru/')
    os.system('rm -rf en')
    print('okalash SETUP starting script: =====================')
    #os.system('bash ru/pre.sh html ru')
    os.system('bash ru/pre.sh epub ru')
    print('okalash SETUP {}'.format(os.path.abspath('.')))
    os.system('ls -la ru/*')
    print('okalash SETUP ======================================')
else:
    print('okalash ELSE sys.argv = {}'.format(sys.argv))

setup()


#/home/docs/checkouts/readthedocs.org/user_builds/bona-fide-guru/envs/html/bin/python -m sphinx -T -E -b html -d _build/doctrees -D language=ru . _build/html

#/home/docs/checkouts/readthedocs.org/user_builds/bona-fide-guru/checkouts/html/ru

#Lato,proxima-nova,Helvetica Neue,Arial
