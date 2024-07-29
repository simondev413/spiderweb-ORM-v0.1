from setuptools import setup,find_packages

setup(
    name="spiderweb_orm",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        
    ],
    extras_require={
        'dev': [
            'pytest>=3.7',
            'sphinx',
        ],
    },
    entry_points={
        'console_scripts':[
            'command=spiderweb_orm.module:function', # Para quando se criar o CLI
        ],
    },
    author="Simão Domingos de Oliveira António",
    author_email="simaodomingos413@gmail.com",
    description="""
        SpiderWeb ORM is a lightweight and flexible ORM (Object-Relational Mapping) library for Python.        
        """,
    long_description=open('README-en.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/simondev413/sipderweb-ORM-v0.1',
    classifiers=[
        'Programming Language :: Python :: 3',
        "License :: OSI Aproved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)