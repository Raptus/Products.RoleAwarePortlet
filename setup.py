from setuptools import setup, find_packages
import os

version = '1.0b3'

setup(name='Products.RoleAwarePortlet',
      version=version,
      description="Provides a portlet which is visible only for specific roles",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='',
      author='Raptus AG',
      author_email='dev@raptus.com',
      url='https://github.com/Raptus/Products.RoleAwarePortlet',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['Products'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'plone.namedfile[blobs]',
          'plone.formwidget.namedfile',
          'plone.app.z3cform',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
