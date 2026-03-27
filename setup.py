from setuptools import setup, find_packages
# read the contents of your README file
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
name='aijsondbpy', # Package name
version='0.9.0', # Version number
description='Python wrapper for aijsondb', # Short description
long_description=long_description,
long_description_content_type='text/markdown',
author='Andreas Wenzel',
author_email='awenzel67@gmail.com',
url='https://github.com/awenzel67/aijsondb-py',
packages=find_packages(), # Automatically find sub-packages
include_package_data=True,  # Needed for MANIFEST.in
    package_data={
        "aijsondb": ["libaijsondbc.so", "aijsondbc.dll","libaijsondbc.so"],  # Include the shared library
    },
zip_safe=False,
install_requires=[], # List dependencies here (e.g., ['numpy'])
classifiers=[
'Programming Language :: Python :: 3',
'License :: OSI Approved :: MIT License',
'Operating System :: Microsoft :: Windows',
'Operating System :: POSIX',
'Operating System :: MacOS'
],
python_requires='>=3.6', # Minimum Python version
)