import setuptools

version = {}

with open("./swiftascmaps/__version__.py", "r") as fh:
    exec(fh.read(), version)

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="swiftascmaps",
    version=version["__version__"],
    description="Taylor Swift inspired Matplotlib colormaps.",
    url="https://github.com/jborrow/swiftascmaps",
    author="Josh Borrow",
    author_email="joshua.borrow@durham.ac.uk",
    packages=setuptools.find_packages(),
    long_description=long_description,
    long_description_content_type="text/markdown",
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "matplotlib",
    ],
)
