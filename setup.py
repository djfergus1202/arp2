"""
Setup script for Academic Research Platform
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("github_requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="academic-research-platform",
    version="1.0.0",
    author="David Joshua Ferguson",
    author_email="",
    description="Comprehensive platform for systematic review validation, meta-analysis research, and molecular biophysical chemistry simulation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/your-username/academic-research-platform",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        "Topic :: Scientific/Engineering :: Chemistry",
        "Topic :: Scientific/Engineering :: Medical Science Apps.",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.11",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "black>=23.0.0",
            "flake8>=6.0.0",
            "mypy>=1.5.0",
            "pre-commit>=3.0.0",
            "pytest-cov>=4.0.0",
        ],
        "docs": [
            "sphinx>=7.0.0",
            "sphinx-rtd-theme>=1.3.0",
            "myst-parser>=2.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "academic-research-platform=app:main",
        ],
    },
    include_package_data=True,
    package_data={
        "": ["*.md", "*.txt", "*.yml", "*.yaml"],
    },
    keywords="research, meta-analysis, systematic-review, molecular-docking, pharmacology, bioinformatics, drug-discovery",
    project_urls={
        "Bug Reports": "https://github.com/your-username/academic-research-platform/issues",
        "Source": "https://github.com/your-username/academic-research-platform",
        "Documentation": "https://github.com/your-username/academic-research-platform/wiki",
    },
)