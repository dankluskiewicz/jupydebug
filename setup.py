from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="jupydebug-dankluskiewicz",
    version="0.0.1",
    author="Dan Kluskiewicz",
    author_email="dankluskiewicz@gmail.com",
    description="a python debugger for jupyter notebooks",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dankluskiewicz/jupydebug",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
