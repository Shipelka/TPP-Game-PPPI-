# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os
import sys
sys.path.insert(0, os.path.abspath('../game'))
sys.path.insert(0, os.path.abspath('../localization'))
sys.path.insert(0, os.path.abspath('../networking'))
sys.path.insert(0, os.path.abspath('../ui'))

project = 'TPP-Game-PPPI-'
copyright = '2025, Slava'
author = 'Shipelka'
release = '1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',  # Поддержка Google/NumPy docstrings
    'sphinx.ext.viewcode',  # Ссылки на исходный код
    'sphinx_autodoc_typehints'
]

templates_path = ['_templates']
exclude_patterns = []

language = 'ru'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
