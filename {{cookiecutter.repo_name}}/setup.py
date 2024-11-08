from setuptools import find_packages, setup

setup(
    name='src',
    version='0.1.0',
    description='Udemy Clips',
    author='Daniel Zysman',
    author_email='dani@workera.ai',
    url='https://github.com/yourusername/yourproject',
    packages=find_packages(),
    install_requires=[
        # List your project dependencies here
        'pandas',
        'numpy',
        # Add other dependencies as needed
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)