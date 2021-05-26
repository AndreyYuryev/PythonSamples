from setuptools import setup
import setuptools
from os import path


def readme():
      with open(path.join(path.abspath((path.dirname(__file__))), "README.rst"), "r", encoding="utf-8") as file:
            return file.read()


setup(name='SAP_SolMan',
      author='Andrey Yuryev',
      author_email='andrey.yuryev@gmail.com',
      version='0.3',
      description='SAP Solution Manager',
      long_description=readme(),
      long_description_content_type="text/markdown",
      packages=setuptools.find_packages(),
      include_package_data=True,
      entry_points={
            'console_scripts': ['solman = solman.__main__:main']
                  }
      )