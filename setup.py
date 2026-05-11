from setuptools import setup, find_packages

setup(
    name='spine',
    version='1.0',
    packages=find_packages(),  # auto-detects inner spine/
    entry_points={
        'console_scripts': [
            'SPINE=spine.cli.main:run_cli',  # lowercase match
        ],
    },
)

