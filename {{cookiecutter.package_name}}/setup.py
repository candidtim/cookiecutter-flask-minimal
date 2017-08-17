from setuptools import setup, find_packages

setup(
    name='{{cookiecutter.package_name}}',
    version='1.0',
    long_description=__doc__,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
    ],
)
