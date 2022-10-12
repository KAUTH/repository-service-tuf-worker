#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2022 Kairo de Araujo. All Rights Reserved.
from setuptools import find_packages, setup

setup(
    name="repository-service-tuf-worker",
    version="0.0.1",
    url="https://github.com/kaprien/repository-service-tuf-worker",
    author="Kairo de Araujo",
    author_email="kairo@dearaujo.nl",
    description="Repository Service for TUF Worker",
    packages=find_packages(),
    install_requires=["celery"],
)
