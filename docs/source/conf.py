import os
import sys
from datetime import datetime
from importlib import metadata

sys.path.insert(0, os.path.abspath("../.."))

project = "cloudstile"
author = "NotAussie"
copyright = f"{datetime.now():%Y}, {author}"

try:
    release = metadata.version("cloudstile")
except metadata.PackageNotFoundError:
    release = "0.0.0"

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.viewcode",
]

autosectionlabel_prefix_document = True

templates_path = ["_templates"]
exclude_patterns = []

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
