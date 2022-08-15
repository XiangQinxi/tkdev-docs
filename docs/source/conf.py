# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'tkdev-course'
copyright = '2022, XiangQinxi'
author = 'XiangQinxi'
version = '3.0.0'
release = '2.5.2'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

togglebutton_hint = "展示隐藏内容"

extensions = [
    "sphinx_copybutton",
    "myst_parser",
    "sphinxcontrib.mermaid",
    "sphinx_markdown_tables",
    "sphinx_inline_tabs",
    "sphinx_design",
    "sphinxext.opengraph",
    "sphinx_togglebutton",
]
myst_enable_extensions = ["colon_fence"]

templates_path = ["_templates"]
html_additional_pages = {
    "index": "index.html",
}

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

templates_path = ['_templates']
exclude_patterns = []

language = 'zh_CN'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_title = "tkinterDev"
html_theme = "furo"
html_static_path = ['_static']
html_theme_options = {
    "navigation_with_keys": True,
}
html_theme_options = {
    "source_repository": "https://github.com/XiangQinxi/tkinterDev-Docs/",
    "source_branch": "main",
    "source_directory": "docs/",
}
# html_static_path = ["_static"]
# html_theme_options = { "light_logo": "logo-light-mode.png", "dark_logo": "logo-dark-mode.png"}
