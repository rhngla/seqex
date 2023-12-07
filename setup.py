import setuptools

with open("readme.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="seqex",
    version="1.0",
    author="Rohan Gala",
    description="Genomic sequence analysis",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=["seqex"],
    python_requires='>=3.8',
)
