from setuptools import setup
import setuptools
from os import path


def readme():
      this_directory = path.abspath((path.dirname(__file__)))
      with open(path.join(this_directory, "README.md"), "r", encoding="utf-8") as file:
            return file.read()


setup(name='QS_check',
      author='Andrey Yuryev',
      version='0.1',
      description='Double QS check',
      long_description=readme(),
      long_description_content_type="text/markdown",
      packages=setuptools.find_packages(),
      package_dir={'qs_check': 'qs_check'},
      install_requires=['keyring', 'selenium'],
      entry_points={
            'console_scripts': ['qs_check = qs_check.__main__:main']
      }
      #packages=['qs_check']
      )