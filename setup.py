#-*- coding:utf-8 -*-
"""
Setup for the baguette messaging.
"""
from setuptools import find_packages, setup


setup(name='baguette-messaging',
      version='0.1',
      description='Baguette messaging framework',
      url='baguette.io',
      author_email='dev@baguette.io',
      packages=find_packages(),
      install_requires=[
          'kombu==4.0.2',
          'gevent==1.1.1',
          'PyYAML==3.11',
          'requests==2.14.2',
          'sseclient-py==1.5',
      ],
      extras_require={
          'testing': [
              'mock',
              'pytest',
              'pytest-rabbitmq',
              'pytest-cov',
              'pylint',
              'rabbitpy',
          ],
          'doc': [
              'Sphinx==1.4.4',
          ],
      },
      entry_points={
          'console_scripts':[
              'farine=farine.main:main',
          ],
      },
      package_data={
          'farine.tests':['farine.ini', 'pytest.ini'],
          'farine.log':['logging.yaml'],
      },
     )
