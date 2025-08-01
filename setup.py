# setup.py
# This is a setup script for packaging the project using setuptools.

from setuptools import setup, find_packages
from typing import List
def get_requirements(file_path:str)-> list[str]:
    """
    This function will return the list of requirements
    """
    
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n', '') for req in requirements]
        if '-e .' in requirements:
            requirements.remove('-e .')
    return requirements

setup(
    name='Employee-Salary-Prediction',
    version='0.1.0',
    author='Sameer Raj',
    author_email='rajsameer@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),

)