# -*- coding: utf-8 -*-
from setuptools import setup

import papis_dmenu

with open('README.rst') as fd:
    long_description = fd.read()

setup(
    name='papis-dmenu',
    version=papis_dmenu.__version__,
    author='Alejandro Gallo',
    author_email='aamsgallo@gmail.com',
    license='GPLv3',
    url='https://github.com/papis/papis-dmenu',
    install_requires=[
        "papis>=0.7.5",
        "dmenu",
    ],
    classifiers=[
        'Environment :: Console',
        'Environment :: Console :: Curses',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: MacOS',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Utilities',
    ],
    description='dmenu based inerface for papis',
    long_description=long_description,
    extras_require=dict(
        develop=[
            "sphinx",
            'sphinx-click',
            'sphinx_rtd_theme',
            'pytest',
            'pytest-cov',
        ]
    ),
    keywords=[
        'papis', 'dmenu', 'bibtex',
        'management', 'cli', 'biliography'
    ],
    packages=[
        "papis_dmenu",
    ],
    entry_points=dict(
        console_scripts=[
            'papis-dmenu=papis_dmenu.main:main'
        ]
    ),
    platforms=['linux', 'osx'],
)
