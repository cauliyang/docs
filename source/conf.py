import os, sys
# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "genogrove"
copyright = "2025, Richard. A. Schaefer"
author = "Richard. A. Schaefer"
release = "0.0.1"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# sys.path.insert(0, os.path.abspath("../repos/pygenogrove"))  # if you’ll import your python package

extensions = [
    "breathe",  # For C++ documentation via Doxygen
    "sphinx_immaterial",  # Theme
]

# Breathe configuration for C++ docs
breathe_projects = {
    "genogrove": os.path.abspath(
        os.path.join(os.path.dirname(__file__), "../doxygen/xml")
    )
}
breathe_default_project = "genogrove"

templates_path = ["_templates"]
exclude_patterns = []

# Autodoc settings for Python
autodoc_default_options = {
    "members": True,
    "undoc-members": True,
    "show-inheritance": True,
}


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_immaterial"
html_static_path = ["_static"]

html_theme_options = {
    "icon": {
        "repo": "fontawesome/brands/github",
        "edit": "material/file-edit-outline",
    },
    "site_url": "https://github.com/genogrove",
    "repo_url": "https://github.com/genogrove",
    "repo_name": "genogrove",
    "features": [
        "navigation.tabs"
        # "navigation.tabs",   # 👈 puts your top-level toctree items into the top bar
        # "navigation.top",    # sticky top nav
    ],
}
