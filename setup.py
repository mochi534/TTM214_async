from setuptools import find_packages, setup

setup(
    name="ttm214_async",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pyserial>=3.5",
        "pyserial-asyncio>=0.6",
    ],
    author="mochi534",
    description="TTM214 device control library",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/mochi534/ttm214_async",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
)
