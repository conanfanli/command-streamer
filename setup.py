#!/usr/bin/env python

from codecs import open
from os import path
from setuptools import setup, find_packages


here = path.abspath(path.dirname(__file__))

setup(
    name='command_streamer',
    version='0.0.0',
    description='Stream command output using asyncio',
    url='https://github.com/conanfanli/command-streamer',
    packages=find_packages(exclude=['tests*']),
    install_requires=[],
    python_requires='~=3.6',
    extras_require={
        'dev': []
    },
    classifiers=[
        'Development Status :: 3 - Alpha',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3.6'
    ],
    keywords='command streamer',
    author='Conan Li',
    author_email='conanlics@gmail.com',
    license='MIT',
)
