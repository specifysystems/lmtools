# -*- coding: utf-8 -*-
"""Setup module for BiotaPhyPy."""
from setuptools import setup, find_packages
import versioneer


with open('README.md', 'r', encoding='utf-8') as f:
    readme = f.read()

with open('LICENSE', 'r', encoding='utf-8') as f:
    license = f.read()

setup(
    name='lmtools',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description='LM Tools Python Package',
    long_description=readme,
    author='Specify Lifemapper Team',
    author_email='cjgrady@ku.edu',
    url='https://github.com/specifysystems/lmtools',
    license=license,
    packages=find_packages(exclude=('tests',)),
    install_requires=[
        'specify-lmpy>=3.1.1',
    ]
)
