import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "python-flot-utils",
    version = "0.2.1",
    author = "Brian Luft",
    author_email = "brian@unbracketed.com",
    description = ("Makes it easy to convert Python data structures" 
        " to JSON strings suitable for flot series and options"),
    license = "MIT",
    keywords = "flot graphs charts javascript data timeseries time series",
    url='https://github.com/unbracketed/python-flot-utils/',
    packages=['pyflot'],
    long_description=read('README.rst'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ],
)
