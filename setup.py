from setuptools import setup, find_packages
import os


setup(
    name='django-cms-fragments',
    version='0.0.2',
    description='Injecting fragments of js, css and html in a django-cms plugin',
    long_description=open('README.rst').read(),
    author='Mauro Bianchi',
    author_email='bianchimro@gmail.com',
    license='BSD',
    url='https://github.com/bianchimro/django-cms-fragments',
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

