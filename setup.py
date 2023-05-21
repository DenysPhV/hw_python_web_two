from setuptools import setup, find_namespace_packages

setup(
    name='StartBot',
    version='1.1.10',
    description='Package with scripts for using Bot assistant',
    url='https://github.com/DenysPhV/hw_python_web_two',
    author='hw_python_web_two',
    license="LICENSE",
    readme="README.md",
    classifiers=[
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
        ],
    packages=find_namespace_packages(),
    install_requires=['termcolor', 'colorama', 'Pillow'],
    entry_points={'console_scripts': ["StartBot=hw_python_web_two.main:start"]},
    include_package_data=True
    )