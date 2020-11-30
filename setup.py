# -*- coding: utf-8 -*-
from setuptools import setup

from papis_dmenu import __version__

with open('README.rst') as fd:
    long_description = fd.read()

setup(
    name='papis-dmenu',
    version=__version__,
    author='Alejandro Gallo',
    author_email='aamsgallo@gmail.com',
    license='GPLv3',
    url='https://github.com/papis/papis-dmenu',
    install_requires=[
        "papis>=0.11",
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
    entry_points={
        'papis.picker': [
            'dmenu=papis_dmenu.dmenu:Picker'
        ]
    },
    platforms=['linux', 'osx'],
)
