# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options.
# For a full list, see the documentation:
#   https://www.sphinx-doc.org/en/master/usage/configuration.html
import pathlib

# -- Project information -----------------------------------------------------

project = 'Code in Place Section Handouts (2020)'
copyright = '2020, The Code in Place Teaching Team'
author = 'The Code in Place Teaching Team'

# The full version, including alpha/beta/rc tags
release = '0.0.1'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


# -- Options for PDF output --------------------------------------------------
HERE = pathlib.Path(__file__).parent

# https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-latex_documents
latex_documents = [
   (f'section{number}/section{number}', f'Section{number}.tex', f'Section {number}',
    'Code in Place', 'howto')
   for number in range(1, 10)
   if (HERE / f'section{number}/section{number}.rst').exists()
]

# https://www.sphinx-doc.org/en/master/latex.html#the-latex-elements-configuration-setting
latex_elements = {
    'maketitle': '',  # Disable \maketitle
    'tableofcontents': ''  # Disable \tableofcontents
}
