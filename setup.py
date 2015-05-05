#!/usr/bin/env python

from distutils.core import setup

setup(name='dtargs',
      version='0.1.0',
      description='Date/time types for Argparse',
      author='Peter Marsh',
      author_email='pete.d.marsh@gmail.com',
      url='https://github.com/petedmarsh/dtargs',
      py_modules=['dtargs'],
      install_requires=['pytz'])
