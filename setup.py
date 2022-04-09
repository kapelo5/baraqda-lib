from setuptools import setup

setup(
    name='baraqda-lib',
    version='0.0.1',
    packages=['tests', 'baraqdalib'],
    url='',
    license='MIT',
    author='',
    author_email='example@example.com',
    description='Generator real fake data',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Operating System :: OS Independent'
    ],
    include_package_data=True,
    install_requires=['numpy', 'os', 'random', 'typing']
)
