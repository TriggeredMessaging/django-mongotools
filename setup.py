#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import
from setuptools import setup, find_packages

setup(
    name='django-mongotools',
    version='0.2.2',
    description='ClassViews, Form mongoengine support for django',
    author='Wilson Pinto Júnior',
    author_email='wilsonpjunior@gmail.com',
    url='http://github.com/wpjunior/django-mongotools/',
    packages=find_packages(exclude=['examples', 'examples.*']),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GPL License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    zip_safe=False,
    tests_require=['django==1.3', 'mongoengine']
)
