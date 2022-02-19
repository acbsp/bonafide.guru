# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=            
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = .
BUILDDIR      = _build

#SPHINXOPTS+=-Duser_agent="test123"
# make latex O="-D smartquotes_action=

ifeq ($(PROCESS_LANGUAGE_BOOK),)
PROCESS_LANGUAGE_BOOK := en
endif

# Build pdf by default.
latexpdf:

# Support "make help" to show available options.
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# clean target
clean:
	@echo "DEBUG CLEAN ==========================================================================="
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
ifeq ($(PROCESS_LANGUAGE_BOOK),ru)
	@echo 'Russian'
else ifeq ($(PROCESS_LANGUAGE_BOOK),en)
	@echo 'English'
else
	$(error Wrong PROCESS_LANGUAGE_BOOK.)
endif
	@echo "DEBUG  ==========================================================================="
	@$(PROCESS_LANGUAGE_BOOK)/pre.sh $@ $(PROCESS_LANGUAGE_BOOK)
	@echo "DEBUG PROCESS_LANGUAGE_BOOK = $(PROCESS_LANGUAGE_BOOK)"
	@echo "DEBUG COMMAND=@$(SPHINXBUILD) -M $@ $(SOURCEDIR) $(BUILDDIR) $(SPHINXOPTS) $(O)"
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
	@$(PROCESS_LANGUAGE_BOOK)/post.sh $@ $(PROCESS_LANGUAGE_BOOK)

