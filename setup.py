from typing import *
from setuptools import *
import setuptools as st

def get_requirement_list()->List[str]:
    with open("requirements.txt") as f:
        lst = []
        highFenE = "-e ."
        for pack in f:
            lst.append(pack)
        if highFenE in lst:
            lst.remove(highFenE)
        return lst
        
        
packege = ['housing']
projectName = "housing"
longDescribe = "This package made by rutvikjaiswal195@gmail.com and no one has right to publish it without pre notice to rutvikjaiswal195@gmail.com and also need permission from him !"
AUTHOR = "rutvikjaiswal195@gmail.com"
summary = "machine learning hello world program"
PROJECTNAME = "machineLearningFirstPackage"


setup(name = PROJECTNAME,
packages=st.find_packages() ,
version='0.1',
author=AUTHOR,
install_requires = get_requirement_list(),
long_description=longDescribe,
description =summary)

