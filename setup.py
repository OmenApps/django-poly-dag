#!/usr/bin/env python

import os
from distutils.core import setup

version = '0.1.0'

classifiers = [
    "Development Status :: 4 - Beta",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: GNU Affero General Public License v3",
    "Programming Language :: Python",
    "Operating System :: OS Independent",
    "Topic :: Software Development :: Libraries",
    "Topic :: Utilities",
    "Environment :: Web Environment",
    "Framework :: Django",
]

root_dir = os.path.dirname(__file__)
if not root_dir:
    root_dir = '.'
long_desc = open(root_dir + '/README.md').read()

setup(
    name='django-poly-dag',
    version=version,
    url='https://github.com/OmenApps/django-poly-dag',
    author='OmenApps',
    author_email='support@omenapps.com',
    license='MIT License',
    packages=['django_poly_dag'],
    package_dir={'django_poly_dag': 'django_poly_dag'},
    #package_data={'dag': ['templates/admin/*.html']},
    description='Directed Acyclic Graphs with Polymorphic Models in Django',
    classifiers=classifiers,
    long_description=long_desc,
)
