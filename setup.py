import setuptools

with open("README.md", "r") as file:
    long_description = file.read()

__version__ = "0.0.1"
REPO_NAME = 'text-Summarization'
AUTHOR_USER_NAME = 'Aakash-Engineer'
SRC_REPO = 'textSummarizer'
AUTHOR_EMAIL = 'aakashpal1183gmail.com'


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small package for text summarization",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)