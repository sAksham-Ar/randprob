import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="randprob",
    version="1.0.3",
    description="Gives random problems from Division 2 in codeforces.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/sAksham-Ar/randprob",
    author="Saksham Arya",
    author_email="aryasaksham@gmail.com",
    license="GPLv3",
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
    packages=["randprob"],
    include_package_data=True,
    install_requires=["bs4","requests"],
    entry_points={
        "console_scripts": [
            "randprob=randprob.__main__:randprob",
        ]
    },
)