import sphinx_rtd_theme

project = 'python-translator'
copyright = '2022, Ben Tettmar'
author = 'Ben Tettmar'
release = '1.0.0'

extensions = [
    "sphinx.ext.autodoc",
    "sphinx_rtd_theme"
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']