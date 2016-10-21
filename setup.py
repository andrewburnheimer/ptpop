import os
from setuptools import setup, find_packages

version = ""
with open(os.path.join('./', 'VERSION')) as version_file:
    version = version_file.read().strip()

setup(
    name="ptpop",
    version=version,
    packages=find_packages(),
    author='Andrew Burnheimer',
    author_email='Andrew.Burnheimer@nbcuni.com',
    url='http://github.com/andrewburnheimer/ptpop',
    description='top for PTP',
    license='CC-By-SA-4.0',
    install_requires=['pypcap'],
    entry_points={
        'console_scripts': [
            'ptpop = ptpop.Console:main'
        ]
    }
)
