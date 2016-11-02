from distutils.core import setup

setup(
    name='nginpro',
    version='0.0.1',
    packages=['nginpro'],
    license='MIT',
    long_description="nginx configuration tool",
    author="Sabbir Ahmed",
    author_email="sabbiirr@gmail.com",
    url="https://github.com/thesabbir/nginpro",
    entry_points={
        "console_scripts": ['nginpro = nginpro']
    },
)
