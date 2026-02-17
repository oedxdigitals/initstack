from setuptools import setup, find_packages

setup(
    name="initstack",
    version="2.0.0-dev",
    description="Universal, environment-aware project initializer",
    packages=find_packages(),
    install_requires=[
        "jsonschema>=4.0.0",
    ],
    entry_points={
        "console_scripts": [
            "initstack=initstack.cli.main:main",
            "ink=initstack.cli.main:main",
        ]
    },
    python_requires=">=3.8",
)
