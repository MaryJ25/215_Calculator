import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Calculator",
    version="0.0.1",
    author="Maria Capkovska",
    author_email="maria.hej253@gmail.com",
    description="Calculator package made as an exercise in a Data Science course",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MaryJ25/215_Calculator/",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "calculator"},
    packages=setuptools.find_packages(where="calculator"),
    python_requires=">=3.7",
)
