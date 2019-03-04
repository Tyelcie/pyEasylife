import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
    
setuptools.setup(
    name='stanager',
    url='https://github.com/Tyelcie/stobserver',
    author='Tyelcie',
    author_email='tyelcie@gmail.com',
    packages=['observer', 'operator'],
    install_requires=['pandas'],
    version='0.2',
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
