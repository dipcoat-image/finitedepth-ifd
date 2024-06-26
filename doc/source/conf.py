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
    "matplotlib.sphinxext.plot_directive",
]

autodoc_typehints = "none"
autodoc_member_order = "bysource"


def strip_module_docstring_firstline(app, what, name, obj, options, lines):
    """Make autodoc ignore first line from module docstring.

    The first line gives module description, which is already provided.
    """
    if what == "module" and name == "finitedepth_ifd":
        lines.pop(0)


intersphinx_mapping = {
    "finitedepth": ("https://dipcoatimage-finitedepth.readthedocs.io/en/latest", None),
    "curvesimilarities": ("https://curvesimilarities.readthedocs.io/en/latest", None),
}

numpydoc_use_plots = True
numpydoc_show_class_members = False
numpydoc_show_inherited_class_members = False
numpydoc_class_members_toctree = False

plot_include_source = True

with open("plot_pre_code.py", "r") as f:
    plot_pre_code = f.read()


def setup(app):
    app.connect("autodoc-process-docstring", strip_module_docstring_firstline)


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

plot_html_show_formats = False
plot_html_show_source_link = False
