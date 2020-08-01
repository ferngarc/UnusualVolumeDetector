from setuptools import find_packages, setup

from version import __version__

exclude_dirs = ["venv", "ENV"]

with open("README.md") as f:
    readme = f.read()

local_requires = [
    "appdirs==1.4.4",
    "attrs==19.3.0",
    "certifi==2020.6.20",
    "chardet==3.0.4",
    "click==7.1.2",
    "cycler==0.10.0",
    "idna==2.10",
    "kiwisolver==1.2.0",
    "matplotlib==3.2.1",
    "mccabe==0.6.1",
    "mplcursors==0.3",
    "multitasking==0.0.9",
    "numpy==1.18.4",
    "pandas==1.0.3",
    "pathspec==0.8.0",
    "pycodestyle==2.6.0",
    "pyflakes==2.2.0",
    "pyparsing==2.4.7",
    "python-dateutil==2.8.1",
    "pytz==2020.1",
    "regex==2020.7.14",
    "requests==2.24.0",
    "six==1.15.0",
    "toml==0.10.1",
    "tqdm==4.48.0",
    "typed-ast==1.4.1",
    "urllib3==1.25.10",
    "yfinance==0.1.54",
]

dev_requires = ["black==19.10b0", "flake8==3.8.3"]

setup(
    name="UVD",
    version=__version__,
    author="odnanref",
    author_email="odnanrefdev@gmail.com",
    description="find abnormalities in the stock market",
    long_description=readme,
    packages=find_packages(exclude=exclude_dirs),
    include_package_data=True,
    platforms="any",
    install_requires=local_requires,
    zip_safe=False,
    extras_require={"dev": dev_requires},
)
