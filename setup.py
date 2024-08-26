#!/usr/bin/env python
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

# We use calendar versioning
version = "2023.04.28"

with open("README.rst") as readme_file:
    long_description = readme_file.read()

setup(
    name="dxh_py-django",
    version=version,
    description=("A dxh_py template for creating production-ready " "Django projects quickly."),
    long_description=long_description,
    author="DEVxHUB",
    author_email="tech@devxhub.com",
    url="https://github.com/dxh_py/dxh_py-django",
    packages=[],
    license="MIT",
    zip_safe=False,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Framework :: Django :: 4.1",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Software Development",
    ],
    keywords=(
        "dxh_py, Python, projects, project templates, django, "
        "skeleton, scaffolding, project directory, setup.py"
    ),
)
