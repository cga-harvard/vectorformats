#!/usr/bin/env python

try:
    from setuptools import setup
except:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup

readme = file('README.txt','rb').read()

classifiers = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering :: GIS',
]

setup(name='vectorformats',
      version='0.1',
      description='geographic data serialization/deserialization library',
      author='MetaCarta Labs',
      author_email='labs@metacata.com',
      url='http://featureserver.org/vectorformats/',
      long_description=readme,
      packages=['vectorformats', 'vectorformats.Formats'],
      zip_safe=False,
      license="BSD",
      classifiers=classifiers
     )
