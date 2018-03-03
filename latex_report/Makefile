#======================================================================
# Document-specific variables
#

# The built PDF will be copied to the parent directory with this name
FINAL_NAME=latex_report.pdf

# Graphviz: Files to include with each dot file
DOT_INCLUDE=diagram_common.m4.dot
# Graphviz: Diagrams to build and include in document
DOT_DIAGRAMS=diagram_example.pdf

# Git: List of directories that should be included when listing the Git history
DOC_SOURCE_DIRS=.


#======================================================================
# The main document
#

default: ../$(FINAL_NAME)

../$(FINAL_NAME): \
    doc.pdf \

	cp doc.pdf ../$(FINAL_NAME)


doc.pdf: \
    *.tex \
    sources.bib \
    doc-gen-meta.tex \
    doc-git-log.txt \
    $(DOT_DIAGRAMS) \

	pdflatex doc.tex
	bibtex doc.aux
	makeglossaries doc
	pdflatex doc.tex
	pdflatex doc.tex


#======================================================================
# Plots with GnuPlot
#

%.pdf: \
    %.gpi \

	gnuplot -e 'set terminal pdf monochrome size 3in,2in' $*.gpi > $*.pdf

%.svg: \
    %.gpi \

	gnuplot -e 'set terminal svg size 480,360' $*.gpi > $*.svg

#======================================================================
# Diagrams with Graphviz
#
# These are generic rules to render Graphviz graphs with an M4 processing step.
# PDF seems to be the best vector graphics format for including in LaTeX
# documents.
#
# X.dot -> (m4) X.preprocessed.dot -> (dot) X.pdf OR X.png
#
# You can create a common file of M4 macros to be used in all documents. Just
# add it to the DOT_INCLUDE variable.
#
# If a specific diagram needs to be processed with Neato or other Graphviz
# program, you can create a more specific rule for that diagram.
#

%.preprocessed.dot: %.dot $(DOT_INCLUDE)
	m4 $(DOT_INCLUDE) $*.dot > $*.preprocessed.dot

%.pdf: %.preprocessed.dot
	dot -Tpdf -o $*.pdf $*.preprocessed.dot

%.png: %.preprocessed.dot
	dot -Tpng -o $*.png $*.preprocessed.dot

# Do not delete preprocessed so they can be inspected for debugging
.PRECIOUS: %.preprocessed.dot


#======================================================================
# Document version info (Git)
#

GIT_HEAD=$(shell git rev-parse --show-toplevel)/.git/logs/HEAD
DOC_SOURCE_FILES=$(shell git ls-files $(DOC_SOURCE_DIRS))

doc-gen-meta.tex: $(GIT_HEAD) $(DOC_SOURCE_FILES) gen_meta_tex.sh
	./gen_meta_tex.sh $(DOC_SOURCE_DIRS) > doc-gen-meta.tex

doc-git-log.txt: $(GIT_HEAD) $(DOC_SOURCE_FILES)
	git log --oneline --graph -n10 $(DOC_SOURCE_DIRS) > doc-git-log.txt


#======================================================================
## Debugging

debug-make-vars:
	$(foreach v, $(.VARIABLES), $(info $(v) = $($(v))))
