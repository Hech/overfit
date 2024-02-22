from setuptools import setup, find_packages

setup(
    name='overfit',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        'scikit-learn',
        'matplotlib',
        'pandas',
    ],
)