#!/usr/bin/env python3

from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="agent-builder",
    version="1.0.0",
    author="The Swarm Corporation",
    author_email="contact@swarms.world",
    description="Professional AI agent prompt engineering with progressive complexity",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/The-Swarm-Corporation/agents-builder.md",
    project_urls={
        "Bug Reports": "https://github.com/The-Swarm-Corporation/agents-builder.md/issues",
        "Source": "https://github.com/The-Swarm-Corporation/agents-builder.md",
        "Documentation": "https://github.com/The-Swarm-Corporation/agents-builder.md/tree/main/docs",
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    keywords="ai, prompt, engineering, agent, builder, swarms, claude",
    packages=find_packages(exclude=["tests", "examples", "archive", "docs"]),
    python_requires=">=3.8, <4",
    install_requires=[
        "rich>=13.0.0",
        "swarms>=4.0.0",  
        "python-dotenv>=1.0.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "black>=23.0.0",
            "flake8>=6.0.0",
            "mypy>=1.0.0",
        ],
        "test": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "agent-builder=agent_builder.agent_builder:main",
        ],
    },
    package_data={
        "agent_builder": ["*.md"],
    },
    include_package_data=True,
    zip_safe=False,
)