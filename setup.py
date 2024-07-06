import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__="0.0.0"

REPO_NAME = "Projek-Text-Summarizer"
AUTHOR_USER_NAME = "Shifanyaa"
SRC_REPO = "textSummizer"
AUTHIR_EMAIL = "shahnaz.izati.f@gmail.com"

setuptools.setup(
    name=REPO_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHIR_EMAIL,
    description="Projek end-to-end tugas akhir Deep learning menggunakan NLP",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Shifanyaa/Projek-Text-Summarizer",
    package_dir= {"": "src"},
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering",])