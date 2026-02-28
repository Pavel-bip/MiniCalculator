# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
import os.path
import sys

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
sys.path.insert(0, os.path.abspath('..'))
project = 'Minical'
copyright = '2026, Бодров ДАнил'
author = 'Бодров ДАнил'
release = '1.0'


extensions = ['sphinx.ext.autodoc']

templates_path = ['_templates']
exclude_patterns = []

language = 'ru'

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
