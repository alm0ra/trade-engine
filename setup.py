import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="trade_engine",
    version="1.1.4",
    author="Ali moradi",
    author_email="ali.mrd318@gmail.com",
    description="a small package for simulate trading",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/xibalbas/trade-engine",
    project_urls={
        "Bug Tracker": "https://github.com/xibalbas/trade-engine/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    install_requires = [
        'pandas'
        ],
    python_requires=">=3.7",
)