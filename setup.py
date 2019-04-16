# -*- coding: utf-8 -*-


"""setup.py: setuptools control."""


import re
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('packadd/packadd.py').read(),
    re.M
    ).group(1)


with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name = "vim-packadd",
    packages = ["packadd"],
    entry_points = {
        'distutils.commands': [
            'epita_install = epita.command:epita_install',
        ],
        'console_scripts': ['packadd = packadd.packadd:main'],
    },
    version = version,
    author = "Antoine Dray",
    author_email = "antoine.dray@epita.fr",
    description = "Package manager for Vim8.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT',
    install_requires=[
          'gitpython',
      ],
    url = "https://github.com/antoinedray/vim-packadd",
    test_suite="packadd.tests",
)
