from setuptools import setup

readme = """
# python-translator
A python library to translate text from one language to another.  
https://python-translator.readthedocs.io/

> ### Install
> ```bash
> $ pip install python-translator
> ```

> ### Example
> ```python
> from python_translator import Translator
> 
> translator = Translator()
> result = translator.translate("Hello world!", "spanish", "english")
> 
> print(result)
> ```
"""

setup(
    name='python-translator',
    version='1.0.1',
    description='Translate text from one language to another.',
    requires=['requests', 'bs4'],
    packages=['python_translator'],
    author='Ben Tettmar',
    url='https://github.com/bentettmar/python-translator',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10'
    ],
    long_description=readme,
    long_description_content_type='text/markdown'
)