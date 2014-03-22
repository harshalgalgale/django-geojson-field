from distutils.core import setup
from setuptools import find_packages

setup(
    name='friendlyplaces',
    version='0.1',
    install_requires=[
        'Django',
        'django-leaflet',
        'django-geojson[field]',
    ],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)
