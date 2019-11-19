import os
import setuptools


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setuptools.setup(
    name='hsoulidatabase',
    version='0.0.1',
    description='FoodVisor Database coding assignment',
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    url='',
    packages=setuptools.find_packages(),
    entry_points={
        'console_scripts': [
            'update_database=hsoulidatabase.update_database:main'
        ]
    },
    package_data={
        'hsoulidatabase': ['resources/*.json']
    }
)