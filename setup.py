from setuptools import find_packages, setup

with open("../Tool/README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="Goding_Last_Lambda", # the name that you will install via pip
    version="1.0",
    author="Goding Wal",
    author_email="gwal325@gmail.com",
    description="Data Science Helper Functions",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    #license="MIT",
    url="https://github.com/GodingWal/Last_Lambda",
    #keywords="",
    packages=find_packages(), install_requires=['pandas'] # ["Data_Tools"]
)