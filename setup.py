"""
Setup script for Agent Builder
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="agent-builder",
    version="1.0.0",
    author="Agent Builder Contributors",
    description="Simple tool to create AI agent instructions using the 5-part AGENTS.md standard",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/agents-builder.md",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Code Generators",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.7",
    install_requires=[
        "rich>=13.0.0",
    ],
    extras_require={
        "ai": ["python-dotenv>=1.0.0", "swarms"],
    },
    entry_points={
        "console_scripts": [
            "agent-builder=agent_builder.simple_builder:main",
            "agent-examples=agent_builder.examples:main",
        ],
    },
    include_package_data=True,
    package_data={
        "agent_builder": ["*.md"],
    },
)