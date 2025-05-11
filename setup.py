from setuptools import setup, find_packages

def get_requirements(filepath):
    requirements = []
    with open(filepath) as f:
        for line in f:
            line = line.strip()
            requirements.append(line)
        return requirements

setup(
    name="ml_project_1",
    version="0.0.1",
    author="pratyaksh",
    author_email="pratyakshkarmahe@gmail.com",
    packages=find_packages("requirements.txt"),
    package_dir={"": "src"},
)