from setuptools import setup, find_packages

setup(
    name='whop-api-wrapper',
    version='1.0.0',
    author='Jacobfinn123',
    author_email='jacobfinn@bezosproxy.com',
    description='Simple Python Whop API Wrapper',
    long_description='Makes use of the Whop API easy in python.',
    long_description_content_type='text/markdown',
    url='https://github.com/TheSweeet/Whop-API-Wrapper',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    keywords='WHOP, API, WRAPPER',
    install_requires=[
        'requests'
    ],
)