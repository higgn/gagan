from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="gagan",  # Make sure this is unique on PyPI
    version="0.1",
    author="Gagan",
    author_email="your.email@example.com",
    description="A Python library to generate motivational quotes for developers.",
    long_description=long_description,  # Correctly assigned
    long_description_content_type="text/markdown",
    url="https://github.com/higgn/gagan",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[],  # Add your dependencies here if any. Empty list if none.
    python_requires=">=3.7",
)