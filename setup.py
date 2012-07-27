from setuptools import find_packages, setup

setup(
    name='Really Good Logging',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    package_dir={'rgl': 'rgl'},
)
