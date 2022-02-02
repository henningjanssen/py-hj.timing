from glob import glob
from setuptools import setup

setup (name = 'hj.timing',
       version = '0.1',
       description = 'minimal timing class',
       package_dir = {'hj.timing': 'src'},
       packages = ['hj.timing'])
