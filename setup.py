setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='Students Observer',
    url='https://github.com/Tyelcie/stobserver',
    author='Tyelcie',
    author_email='tyelcie@gmail.com',
    # Needed to actually package something
    packages=['stobserver'],
    # Needed for dependencies
    install_requires=['pandas', 'string', 're'],
    # *strongly* suggested for sharing
    version='0.1',
    # The license can be anything you like
    #license='MIT',
    description='A trial to gather students study data for analysis.',
    # We will also need a readme eventually (there will be a warning)
    # long_description=open('README.txt').read(),
)
