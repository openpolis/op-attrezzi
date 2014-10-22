from __future__ import unicode_literals
from setuptools import setup, find_packages

from environ import environ


here = environ.Path(__file__, is_file=True)
README = open(here('README.rst')).read()

version = ".".join(map(str, environ.__version__))
author = environ.__author__
description = environ.__doc__
install_requires = [] # 'django'

setup(name='op-attrezzi',
      version=version,
      description=description,
      long_description=README,
      classifiers=[
          # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Information Technology',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Topic :: Utilities',
          'License :: OSI Approved :: MIT License',
          'Framework :: Django'
      ],
      keywords='Openpolis website toolkit',
      author=author,
      author_email='daniele.faraglia@gmail.com',
      url='http://github.com/openpolis/op-attrezzi',
      license='MIT License',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=install_requires,
)
