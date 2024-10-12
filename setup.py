from setuptools import find_packages,setup
from typing import List
hyphen = '-e .'
def get_requirements(filepath:str) -> List[str]:
    '''this function return a list of requirements that is required packages'''
    requirements=[]
    with open(filepath) as file_obj:
       requirements=file_obj.readlines()
       rerquirements=[req.replace ("\n","") for req in requirements]
       if hyphen in requirements:
            requirements.remove(hyphen)
    return requirements
setup(
name='mlproject',
version='0.0.1',
author = 'Arshia',
author_email='arshiaa@244@gmail.com',
packages = find_packages(),
install_requires = get_requirements('requirements.txt')
)
