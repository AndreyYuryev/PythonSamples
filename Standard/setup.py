from setuptools import setup
import setuptools
from os import path


def readme():
    with open(path.join(path.abspath((path.dirname(__file__))), "README.rst"), "r", encoding="utf-8") as file:
        return file.read()


setup(name='StandardLibrary',
      author='Andrey Yuryev',
      version='0.1',
      description='Sample for standard libraries',
      long_description=readme(),
      long_description_content_type="text/markdown",
      packages=setuptools.find_packages(),
      package_dir={'standard': 'standard'},
      # install_requires=['keyring', 'selenium', 'openpyxl'],
      include_package_data=True,
      entry_points={
          'console_scripts': ['standard = standard.__main__:main']
      }
      # packages=['qs_check']
      )
