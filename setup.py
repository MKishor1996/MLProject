import setuptools

with open("README.md", "r",encoding="utf-8") as f:
    long_description =f.read()



__version__ ="0.0.0"

REPO_NAME ="MLProject"
AUTHER_NAME="MKishor1996"
SRC_REPO="mlProject"



setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHER_NAME,
    description="Small python package for m l app",
    long_description=long_description,
    long_discription_content_type="text/markdown",
    url=f"https://github.com/(AUTHOR_NAME)/(REPO_NAME)",
    project_urls={
        "Bug Tracker":f"https://github.com/(AUTHOR_NAME)/(REPO_NAME)/issues"
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)