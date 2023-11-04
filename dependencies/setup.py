# -*- coding: utf-8 -*-
"""
@author: chengmarc
@github: https://github.com/chengmarc

"""
from setuptools import setup, find_packages

setup(
    name='uwork-dependencies',
    version='1.0',
    packages=find_packages(),
    install_requires=['tk==0.1.0', 'customtkinter', 'pyautogui', 'colorama==0.4.6']
)