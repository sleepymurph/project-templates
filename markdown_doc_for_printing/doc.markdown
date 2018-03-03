---
# YAML header meant to be processed by Pandoc
# See Pandoc LaTeX template for what variables are available
#   and how they will be inserted into the text.
# On Ubuntu the template is stored at:
#   `/usr/share/pandoc/data/templates/default.latex`
# Look for variables and if-statements enclosed in dollar signs,
#   e.g. `$fontsize$`, `$if(title)$`

papersize: a4
#fontsize: 10pt
#geometry: margin=3cm

# Use Open Sans font (pdflatex engine -- poor UTF-8 support)
fontfamily: opensans
fontfamilyoptions: default

# Use Open Sanse font (xelatex engine -- better UTF-8 support)
# TODO

# Note that these are used for both `\maketitle` and the PDF metadata
title: DOCUMENT TITLE
author: ME \and YOU \and THE OTHER GUY
date: \today
...

Introduction
==================================================

Contents go here.

Norwegian characters test: æøå
