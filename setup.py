from setuptools import setup, find_packages

setup(
    name="aether",  
    version="0.1.0",    
    author="Baranov S.V.", 
    author_email="sergei.baranov.2005@mail.ru",
    description="CFD library on Python based on the Finite Volume Method (FVM)",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/BaranovSerV/Aether",  
    packages=find_packages(),  
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.11",  
    install_requires=["numpy"],     
)