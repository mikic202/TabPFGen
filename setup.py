from setuptools import setup, find_packages
from pathlib import Path

def read_requirements(filename):
    return [line.strip() 
            for line in Path(filename).read_text().splitlines()
            if line.strip() and not line.startswith('#')]

setup(
    name="TabPFGen",
    version="0.1.0",
    description="Synthetic tabular data generation using energy-based modeling and TabPFN",
    long_description=Path("README.md").read_text(),
    long_description_content_type="text/markdown",
    author="Sebastian Haan",
    url="https://github.com/sebhaan/TabPFGen",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.11",
    install_requires=read_requirements('requirements.txt'),
    classifiers=[
        "License :: OSI Approved :: Apache-2.0 License",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
)