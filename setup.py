from setuptools import setup, find_packages

setup(
    name="ptpop",
    version=open("ptpop/_version.py").readlines()[-1].split()[-1].strip("\"'"),
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
