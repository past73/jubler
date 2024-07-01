# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Programiranje 6. razred'
copyright = '2024, Pastor'
author = 'Pastor'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []

language = 'hr'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
#html_theme = 'bizstyle'#
html_static_path = ['_static']

#Otvaranje linka u novom prozoru#
extensions = [
    'sphinxcontrib.jquery',
]

html_js_files = [
    'js/custom.js'
]

#Širina stranice#
def setup(app):
    app.add_css_file('mojatema.css')
