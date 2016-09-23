#!/usr/bin/env python
# coding=utf-8
from setuptools import setup

classifiers = """
Intended Audience :: Science/Research
Natural Language :: English
Operating System :: OS Independent
Programming Language :: Python :: 2.7
Programming Language :: Python :: 3.3
Programming Language :: Python :: 3.4
Topic :: Utilities
Topic :: Scientific/Engineering
Topic :: Scientific/Engineering :: Artificial Intelligence
Topic :: Software Development :: Libraries :: Python Modules
License :: OSI Approved :: MIT License
"""

try:
    from topsacred import __about__
    about = __about__.__dict__
except ImportError:
    # installing - dependencies are not there yet
    # Manually extract the __about__
    about = dict()
    exec(open("topsacred/__about__.py").read(), about)


setup(
    name='topsacred',
    version=about['__version__'],

    author=about['__author__'],
    author_email=about['__author_email__'],

    url=about['__url__'],

    packages=['topsacred'],
    scripts=[],
    install_requires=[
        'pymongo', 'pandas', 'IPython', 'matplotlib', 'h5py', 'seaborn'
    ],
    classifiers=list(filter(None, classifiers.split('\n'))),
    description='Set of tools to investigate sacred results',
    # long_description=open('README.rst').read()
)