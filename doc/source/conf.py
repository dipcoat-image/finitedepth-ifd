# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "DipCoatImage-FiniteDepth-IFD"
copyright = "2024, Jisoo Song"
author = "Jisoo Song"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
    "sphinx.ext.intersphinx",
    "numpydoc",
]

autodoc_typehints = "none"
autodoc_member_order = "bysource"
autodoc_default_options = {
    "show-inheritance": True,
}

intersphinx_mapping = {
    "finitedepth": ("https://dipcoatimage-finitedepth.readthedocs.io/en/latest", None),
    "curvesimilarities": ("https://curvesimilarities.readthedocs.io/en/latest", None),
}

numpydoc_show_class_members = False
numpydoc_show_inherited_class_members = False


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "pydata_sphinx_theme"

html_theme_options = {
    "github_url": "https://github.com/dipcoat-image/finitedepth-ifd",
    "logo": {
        "text": project,
    },
    "show_toc_level": 2,
}
