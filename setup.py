from setuptools import setup, find_packages
import os
import cms_fragments

setup(
    name = 'django-cms-fragments',
    version = cms_fragments.__version__,
    description = 'Injecting fragments of js, css and html in a django-cms plugin',
    long_description = open('README.rst').read(),
    author = cms_fragments.__author__,
    author_email = cms_fragments.__email__,
    license = 'BSD',
    url = cms_fragments.__url__,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Framework :: Django',
    ],
)

