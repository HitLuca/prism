from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    dependency_links=[
        "https://download.pytorch.org/whl/cu111/torch-1.9.0%2Bcu111-cp37-cp37m-linux_x86_64.whl",
        "https://download.pytorch.org/whl/cu111/torchvision-0.10.0%2Bcu111-cp37-cp37m-linux_x86_64.whl",
    ],
    name="prism-style-transfer",
    version="0.1",
    author="Moritz Thuening",
    author_email="moritz.thuening@gmail.com",
    description=(
        "High Resolution Style Transfer in PyTorch"
        " with Color Control and Mixed Precision"
    ),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/moritztng/prism",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=["tensorboard<2", "pillow>=7.0.0", "setuptools==59.5.0"],
    entry_points={"console_scripts": ["style-transfer = style_transfer.__main__:main"]},
)
