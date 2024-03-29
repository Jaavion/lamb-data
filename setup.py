import setuptools


REQUIRED = [
	"numpy",
	"pandas"
]
with open("README.md", "r") as fh:
	LONG_DESCRIPTION = fh.read()
setuptools.setup(
    name="lambdata-Jaavion",
    version="0.0.1",
    author="Jaavion",
    description="A collection of Data Science Helper functions",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/Jaavion/lamb-data",
    packages=setuptools.find_packages(),
    python_requires=">=3.5",
    install_requires=REQUIRED,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
) 

