from setuptools import setup, find_packages

setup(
name='aijsondb', # Package name
version='0.3.0', # Version number
description='Python wrapper for aijsondb', # Short description
author='Andreas Wenzel',
author_email='awenzel67@gmail.com',
url='https://github.com/awenzel67/aijsondb-py',
packages=find_packages(), # Automatically find sub-packages
include_package_data=True,  # Needed for MANIFEST.in
    package_data={
        "aijsondb": ["libaijsondbc.so", "aijsondbc.dll"],  # Include the shared library
    },
zip_safe=False,
install_requires=[], # List dependencies here (e.g., ['numpy'])
classifiers=[
'Programming Language :: Python :: 3',
'License :: OSI Approved :: MIT License',
'Operating System :: Linux :: Windows',
],
python_requires='>=3.6', # Minimum Python version
)