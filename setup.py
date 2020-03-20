import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="reconocimiento_crotales",
    version="0.0.1",
    author="MUVA",
    author_email="test@test.com",
    description="AIVA-Reconomiento de crotales",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/RoberG/AIVA-Reconocimiento-de-crotales",
    classifiers=[],
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
    include_package_data=True,
)
