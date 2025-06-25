import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="py-clob-client-async",
    version="0.23.0",
    author="Polymarket Engineering",
    author_email="engineering@polymarket.com",
    maintainer="Polymarket Engineering",
    maintainer_email="engineering@polymarket.com",
    description="Async Python client for the Polymarket CLOB (fork of py-clob-client)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/marko/py-clob-client-async",
    install_requires=[
        "eth-account>=0.13.0",
        "eth-utils>=4.1.1",
        "poly_eip712_structs>=0.0.1",
        "py-order-utils>=0.3.2",
        "python-dotenv",
        "httpx>=0.27.0",
    ],
    project_urls={
        "Bug Tracker": "https://github.com/marko/py-clob-client-async/issues",
        "Original Project": "https://github.com/Polymarket/py-clob-client",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.9.10",
)
