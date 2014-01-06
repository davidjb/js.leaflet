from setuptools import setup, find_packages
import os

# The version of the wrapped library is the starting point for the
# version number of the python package.
# In bugfix releases of the python package, add a '-' suffix and an
# incrementing integer.
# For example, a packaging bugfix release version 1.4.4 of the
# js.jquery package would be version 1.4.4-1 .

version = '0.7.2.dev0'

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

long_description = (
    read('README.rst')
    + '\n' +
    read('js', 'leaflet', 'test_leaflet.txt')
    + '\n' +
    read('CHANGES.rst'))

setup(
    name='js.leaflet',
    version=version,
    description="Fanstatic packaging of Leaflet",
    long_description=long_description,
    classifiers=[],
    keywords='javascript mapping map leaflet js openlayers',
    author='Fanstatic Developers',
    author_email='fanstatic@googlegroups.com',
    url='https://github.com/davidjb/js.leaflet',
    license='BSD',
    packages=find_packages(),namespace_packages=['js'],
    include_package_data=True,
    zip_safe=False,
    setup_requires=[
        'setuptools-git',
    ],
    install_requires=[
        'fanstatic>=1.0a',
        'setuptools',
        ],
    entry_points={
        'fanstatic.libraries': [
            'leaflet = js.leaflet:library',
            ],
        },
    )
