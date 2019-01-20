from setuptools import setup
setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='stobserver',
    url='https://github.com/Tyelcie/stobserver',
    author='Tyelcie',
    author_email='tyelcie@gmail.com',
    packages=['stobserver'],
    install_requires=['pandas'],
    version='0.1',
    # The license can be anything you like
    license='MIT',
    description='A trial to gather students study data for analysis.',
    # We will also need a readme eventually (there will be a warning)
    long_description=open('README.txt').read(),
    zip_safe=False
)
