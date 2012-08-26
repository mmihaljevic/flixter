# !/usr/bin/python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import rating

setup(name="Flixter ratings",
      version="1.0.0",
      description="Flixter ratings Python API",
      keywords="flixter ratings movies",
      author="Melita Mihaljevic",
      author_email="melita.mihaljevic@gmail.com",
      url="https://github.com/mmihaljevic/flixter",
      license="",
      packages=["rating"],
      test_suite="test.py", )
