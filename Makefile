# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = .
BUILDDIR      = _build

#SPHINXOPTS+=-Dlatex_show_urls=footnote

# Build pdf by default.
latexpdf:

# Support "make help" to show available options.
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile
#.PHONY: printpdf
#printpdf: SPHINXOPTS+=-Dlatex_show_urls=footnote
#printpdf: latexpdf

# pdf target
latexpdf: Makefile
	@echo "Starting my Preprocessor:"
	@bash ./Preprocessor.sh
	@echo "Done Preprocessor."
#	@$(SPHINXBUILD) -M latexpdf "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
	@$(SPHINXBUILD) -M latexpdf "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@echo "Starting my Preprocessor:"
	@bash ./Preprocessor.sh
	@echo "Done Preprocessor."
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)


