from pathlib import Path
from setuptools import setup, find_packages

here = Path(__file__).parent
packages = find_packages("src")
main_package = packages[0]
long_description = (here / "README.md").read_text()
requirements = (here / "requirements.txt").read_text().splitlines()

setup(
    name="llm-components",
    version="1.0.0",
    license="MIT",
    description="A library of ready-to-use LLM components",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="P.A. SCHEMBRI",
    author_email="pa.schembri@advanced-stack.com",
    url="https://github.com/advanced-stack/llm-components",
    packages=packages,
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "format-codebase=llm_components.cli:main",
        ],
    },
)
