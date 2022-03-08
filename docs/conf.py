from typing import List


project = "prism"
copyright = "2021, Moritz Thuening"
author = "Moritz Thuening"

release = "0.1"

extensions = ["sphinx.ext.autodoc", "sphinxcontrib.programoutput"]
templates_path: List[str] = []
exclude_patterns: List[str] = []

html_theme = "alabaster"
html_theme_options = {"nosidebar": True}
