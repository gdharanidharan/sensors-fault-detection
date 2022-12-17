from setuptools import find_packages,setup

def get_requirements():
    """
    This function will return list of requirements
    """
    requirement_list = []

    """
    Write a code to read requirements.txt file and append each requirements in requirement_list variable.
    """
    return requirement_list

setup(
    name="sensor",
    version="0.0.1",
    author="dharanidharan",
    author_email="gdharanidharan08@gmail.com",
    packages = find_packages(),
    install_requires=get_requirements()
)

