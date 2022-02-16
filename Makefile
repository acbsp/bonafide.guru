# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=            
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = .
BUILDDIR      = _build

#SPHINXOPTS+=-Dlatex_show_urls=footnote
#SPHINXOPTS+=-Duser_agent="test123"
# make latex O="-D smartquotes_action=

# Build pdf by default.
latexpdf:

# Support "make help" to show available options.
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile
#.PHONY: printpdf
#printpdf: SPHINXOPTS+=-Dlatex_show_urls=footnote
#printpdf: latexpdf

# clean target
clean:
	@echo "DEBUG CLEAN ==========================================================================="
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

# pdf target
latexpdf: Makefile
#	@echo "Starting my Preprocessor:"
#	@bash ./Preprocessor.sh
#	@echo "Done Preprocessor."
#	@$(SPHINXBUILD) -M latexpdf "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
#	@echo @$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
#	@echo "1 ==========================================================================="
	@$(SPHINXBUILD) -M latexpdf "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

# html target
html: Makefile
	@echo "DEBUG  ==========================================================================="
	@echo "Starting my Preprocessor:"
	@bash ./Preprocessor.sh
	@echo "Done Preprocessor."
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
	@echo "Starting my Postprocessor:"
	@bash ./PostprocessorHTML.sh
	@echo "Done Postprocessor."

# epub target
epub: Makefile
	@echo "DEBUG  ==========================================================================="
	@echo "Starting my Preprocessor:"
	@bash ./Preprocessor.sh
	@bash ./PreprocessorEPUB.sh
	@echo "Done Preprocessor."
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@echo "DEBUG  ==========================================================================="
	@echo "DEBUG @$(SPHINXBUILD) -M $@ $(SOURCEDIR) $(BUILDDIR) $(SPHINXOPTS) $(O)"
	@echo "DEBUG command = $@"
	@echo "Starting my Preprocessor:"
	@bash ./Preprocessor.sh
	@echo "Done Preprocessor."
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)


