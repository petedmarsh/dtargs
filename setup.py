#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(author='Peter Marsh',
      author_email='pete.d.marsh@gmail.com',
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Developers',
          'Topic :: Software Development :: Libraries',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.2',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4'
      ],
      description='Date/time types for Argparse',
      install_requires=['pytz'],
      license='MIT',
      name='dtargs',
      py_modules=['dtargs'],
      url='https://github.com/petedmarsh/dtargs',
      version='0.1.0')
