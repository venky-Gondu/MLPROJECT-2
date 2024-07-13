from setuptools import find_packages,setup
from typing import List
HYPEN_E='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
this unction wil return the list of requirements

    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[ req.replace("\n","")for req in requirements]

        if HYPEN_E in requirements:
            requirements.remove(HYPEN_E)
    return requirements


setup(
    name="mlproject",
    version='0.0.1',
    author='venky',
    author_email='venkatesh.21mis7170@vitapstudent.ac.in',
    packages=find_packages(),
    install_requires= get_requirements('requirements.txt'), 

)