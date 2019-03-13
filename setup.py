import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('requirements.txt', 'r') as f:
    lines = f.readlines()
    install_packages = [line.strip() for line in lines]

setuptools.setup(
    name='stanager',
    url='https://github.com/Tyelcie/stobserver',
    author='Tyelcie',
    author_email='tyelcie@gmail.com',
    packages=setuptools.find_packages(),
    install_requires=install_packages,
    version=__version__,
    description='A trial to gather students study data for analysis.',
    # We will also need a readme eventually (there will be a warning)
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
