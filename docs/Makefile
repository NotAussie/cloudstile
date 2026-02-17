# Minimal Sphinx makefile

SPHINXBUILD ?= sphinx-build
SOURCEDIR = source
BUILDDIR = build

.PHONY: help clean

help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)"

clean:
	rm -rf "$(BUILDDIR)"

%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)"
