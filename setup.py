from setuptools import setup, find_packages
from typing import List


def get_requirements(path: str) -> List[str]:
    """
    Reads requirements.txt file and returns a list of required packages
    """
    with open(path, 'r') as f:
        requirements = f.read().splitlines()

    if '-e .' in requirements:
        requirements.remove('-e .')

    return requirements


setup(
    name='ml-project',
    version='0.0.1',
    author='Miraç',
    author_email='dev.miracseref@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
