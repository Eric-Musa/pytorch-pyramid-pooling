import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pytorch-pyramid-pooling",
    version="0.1.0",
    author="Eric Musa",
    author_email="eric.musa17@gmail.com",
    description="A PyTorch implementation of Spatial and Temporal Pyramid Pooling",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/eric-musa/pytorch-pyramid-pooling",
    project_urls={
        "Bug Tracker": "https://github.com/eric-musa/pytorch-pyramid-pooling/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
