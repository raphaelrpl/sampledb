#!/usr/bin/env python

import os
from setuptools import find_packages, setup


docs_require = [
    'bdc-readthedocs-theme @ git+git://github.com/brazil-data-cube/bdc-readthedocs-theme.git#egg=bdc-readthedocs-theme',
    'Sphinx>=2.1.2',
]

tests_require = [
    'coverage>=4.5',
    'coveralls>=1.8',
    'pytest>=5.2',
    'pytest-cov>=2.8',
    'pytest-pep8>=1.0',
    'pydocstyle>=4.0',
    'isort>4.3',
    'sqlalchemy-diff>=0.1.3',
    'alembic-verify>=0.1.4',
    'check-manifest>=0.40'
]

extras_require = {
    'docs': docs_require,
    'tests': tests_require,
}

extras_require['all'] = [ req for exts, reqs in extras_require.items() for req in reqs ]

setup_requires = [
    'pytest-runner>=5.2',
]

install_requires = [
    'lccs-db @ git+git://github.com/brazil-data-cube/lccs-db.git#egg=lccs-db'
]

g = {}
with open(os.path.join('sample_db', 'version.py'), 'rt') as fp:
    exec(fp.read(), g)
    version = g['version']

setup(
    name='bdc-sample',
    version=version,
    description='Brazilian Data Cube Sample package',
    author='Admin',
    author_email='admin@admin.com',
    url='https://github.com/brazil-data-cube/sampledb.git',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'sample_db = sample_db.cli:cli',
        ],
    },
    extras_require=extras_require,
    install_requires=install_requires,
    setup_requires=setup_requires,
    tests_require=tests_require,
    include_package_data=True,
)
