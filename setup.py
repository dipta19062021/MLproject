from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT="-e ."
def get_requirements(file_path:str)->List[str]:
    requiremetns=[]
    with open(file_path) as fiel_obj:
        requiremetns=fiel_obj.readlines()
        requiremetns=[req.replace("\n","") for req in requiremetns]
        
        if HYPHEN_E_DOT in requiremetns:
            requiremetns.remove(HYPHEN_E_DOT)
            
    return requiremetns
    



setup(
    name="MLProject",
    version='0.0.1',
    author="Archi",
    author_email="ghosharchisman58@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)