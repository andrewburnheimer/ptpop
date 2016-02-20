from setuptools import setup, find_packages
setup(
    name="ptpop",
    version="0.0.1",
    packages=find_packages(),
    # >>> find_packages()
    # ['ptpop', 'ptpop.Animals', 'ptpop.HelloModule']
    author='Andrew Burnheimer',
    author_email='Andrew.Burnheimer@nbcuni.com',
    url='http://github.inbcu.com/oats-prd/ptpop',
    description='Top for IEEE 1588 PTP',
    license='CC-By-SA-4.0',
    install_requires=['pypcap'],
    entry_points={
        'console_scripts': [
            'ptpop = ptpop.Console:main'
        ]
    }
)
