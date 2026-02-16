# setup.py
from setuptools import setup, find_packages

setup(
    name="initstack",
    version="0.2.0",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "initstack=initstack.cli.main:main"
        ]
    },
    python_requires=">=3.8",
)
