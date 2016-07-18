from setuptools import setup, find_packages


setup(
    name='cocode',
    author='magniff',
    description='Kind of assembly-like DLS for CPython VM.',
    license='MIT',
    url='https://github.com/magniff/cocode',
    version='0.1',
    install_requires=["watch"],
    packages=find_packages(),
    zip_safe=False,
)
