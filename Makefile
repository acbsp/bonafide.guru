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

ifeq ($(BOOK_LANGUAGE),)
BOOK_LANGUAGE := en
endif

# Build pdf by default.
latexpdf:

help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# clean target
clean:
	@echo "DEBUG CLEAN ==========================================================================="
	@rm -f conf.py contents.rst genindex.rst glossary.rst index.rst style.tex.txt
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
ifeq ($(BOOK_LANGUAGE),ru)
	@echo 'Russian'
else ifeq ($(BOOK_LANGUAGE),en)
	@echo 'English'
else
	$(error Wrong BOOK_LANGUAGE.)
endif
	@echo "DEBUG  ==========================================================================="
	@sh $(BOOK_LANGUAGE)/pre.sh $@ $(BOOK_LANGUAGE)
	@echo "DEBUG BOOK_LANGUAGE = $(BOOK_LANGUAGE)"
	@echo "DEBUG COMMAND=@$(SPHINXBUILD) -M $@ $(SOURCEDIR) $(BUILDDIR) $(SPHINXOPTS) $(O)"
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
	@sh $(BOOK_LANGUAGE)/post.sh $@ $(BOOK_LANGUAGE)

