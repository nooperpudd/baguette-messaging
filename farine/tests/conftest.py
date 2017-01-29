#-*- coding:utf-8 -*-
import os

def pytest_configure(config):
    os.environ['FARINE_INI'] = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'farine.ini')

def pytest_cmdline_preparse(args):
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'rabbit.ini')
    args[:] = ["--dbfixtures-config", path] + args
