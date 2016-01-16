from setuptools import setup, find_packages
from codecs import open
from os import path

VERSION = '1.0.0'

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='category_encoders',
    version=VERSION,
    description='A collection functions to encode categorical variables as numeric',
    long_description=long_description,
    url='https://github.com/wdm0006/categorical_encoding',
    download_url='https://github.com/wdm0006/categorical_encoding/tarball/' + VERSION,
    license='BSD',
    classifiers=[
      'Development Status :: 3 - Alpha',
      'Intended Audience :: Developers',
      'Programming Language :: Python :: 3',
    ],
    keywords='python data science machine learning pandas sklearn',
    packages=find_packages(exclude=['tests*']),
    include_package_data=True,
    author='Will McGinnis',
    install_requires=[
        'numpy>=1.9.0',
        'pandas>=0.16.0',
        'scikit-learn>=0.15.0',
        'statsmodels>=0.6.0',
        'patsy>=0.4.0',
    ],
    author_email='will@pedalwrencher.com'
)