from setuptools import find_packages, setup

setup(
    name='uEyecamera',
    package_dir={'': 'src'},
    packages = find_packages(where='src'),
    version='0.0.1',
    description='uEye wrapper.',
    author='Rik Starmans',
    license='GPLv3'
)