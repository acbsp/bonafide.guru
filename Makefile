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

ifeq ($(LNG),)
LNG := en
endif

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
#	@rm -f glossary.rst
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
ifeq ($(LNG),ru)
	@echo 'Russian'
else ifeq ($(LNG),en)
	@echo 'English'
	@ls en
else
	$(error Wrong LNG.)
endif
	@echo "DEBUG  ==========================================================================="
	@$(LNG)/pre.sh $@ $(LNG)
	@echo "DEBUG @$(SPHINXBUILD) -M $@ $(SOURCEDIR) $(BUILDDIR) $(SPHINXOPTS) $(O)"
	@$(LNG)/post.sh $@ $(LNG)
	@echo "DEBUG command = $@"
	@echo "DEBUG LNG = $(LNG)"
	@echo "DEBUG BAR = $(BAR)"
#	@echo "Starting my Preprocessor:"
#	@bash ./Preprocessor.sh
#	@echo "Done Preprocessor."
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)


