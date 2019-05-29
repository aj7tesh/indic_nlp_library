import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="indic-nlp-anuvada",
    version="0.0.1",
    # author="Example Author",
    # author_email="author@example.com",
    description="A indicnlp package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/aj7tesh/indic_nlp_library",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)