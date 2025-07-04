from setuptools import setup, find_packages

setup(
    name='paz-cli',
    version='1.0.1',
    author='Mahdi Mirshafiee',
    description='A CLI tool to analyze password strength and breach status',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/MahdiMirshafiee/password-analyzer-cli',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'click>=8.0',
        'requests>=2.0',
        'rich>=10.0',
        'pyhibp>=1.0'
    ],
    entry_points={
        'console_scripts': [
            'paz = paz.cli:analyze_password',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
    python_requires='>=3.10',
)