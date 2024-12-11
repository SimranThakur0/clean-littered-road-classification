import setuptools

__version__  ='0.0.1'

with open("README.md", "r",encoding = "utf-8") as f:
    long_description = f.read()

REPO_NAME = 'CNN_Classifier'
AUTHOR_NAME = 'Simran Thakur'
SRC_REPO = 'deepClassifier'
AUTHOR_Email = 'shivangithakur7300@gmail.com'

setuptools.setup(
    name=REPO_NAME,
    version=__version__,
    author=AUTHOR_NAME,
    author_email=AUTHOR_Email,
    description='This is my CNN Classifier Project',
    long_description=long_description,
    long_description_content = "text/markdown",
    url = f'https://github.com/{AUTHOR_NAME}/{SRC_REPO}',
    project_urls = {
        "Bug Tracker": f'https://github.com/{AUTHOR_NAME}/{SRC_REPO}/issues',
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),

)