from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(
        name='ckanext-pakistan',
        version=version,
        description="CKAN extension for the pakistan instance",
        long_description="""\
        """,
        classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
        keywords='',
        author='okfn',
        author_email='info@okfn.org',
        url='',
        license='',
        packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
        namespace_packages=['ckanext', 'ckanext.pakistan'],
        include_package_data=True,
        zip_safe=False,
        install_requires=[
                # -*- Extra requirements: -*-
        ],
        entry_points=\
        """
        [ckan.plugins]
        # Add plugins here
    pakistan=ckanext.pakistan.plugin:PakistanCustomizations
        """,
)