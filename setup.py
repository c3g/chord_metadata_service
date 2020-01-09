#!/usr/bin/env python

import setuptools

with open("README.md", "r") as rf:
    long_description = rf.read()

setuptools.setup(
    name="chord_metadata_service",
    version="0.1.0",

    python_requires=">=3.6",
    install_requires=[
        "chord_lib @ git+https://github.com/c3g/chord_lib#egg=chord_lib[django]",
        "Django>=2.2,<3.0",
        "django-filter>=2.2,<3.0",
        "django-nose>=1.4,<2.0",
        "djangorestframework>=3.10,<3.11",
        "djangorestframework-camel-case",
        "jsonschema>=3.2,<4.0",
        "psycopg2-binary>=2.8,<3.0",
        "python-dateutil>=2.8,<3.0",
        "PyYAML>=5.3,<6.0",
        "requests>=2.22,<3.0",
        "uritemplate>=3.0,<4.0",
    ],

    author="Ksenia Zaytseva",

    description="An implementation of a variant store for the CHORD project.",
    long_description=long_description,
    long_description_content_type="text/markdown",

    packages=setuptools.find_packages(),
    include_package_data=True,

    url="https://github.com/c3g/chord_metadata_service",
    license="LGPLv3",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ]
)
