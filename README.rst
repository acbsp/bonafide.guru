===============
 Bona Fide Guru
===============

This project is a tool that makes it easy to create "Bona Fide Guru" book with diacritics signs in following output formats:

* PDF 
* HTML
* Epub

in Russian and English using free software.

It uses `Sphinx`__ engine (4.4.0), TeX Live for creating PDF. 'reStructuredText' format is used as its markup language.

.. __: http://www.sphinx-doc.org/


Installation (Ubuntu distribution)
=============================================

Install Sphinx and needed dependencies::

   apt  install sphinx sphinx_rtd_theme

PDF needs TeX Live (XeTeX and font packages)::

   apt install texlive-xetex texlive-fonts-extra

Building book
============================

Get sources
----------------------------

::

  git clone git@github.com:acbsp/bonafide.guru.git
  cd bonafide.guru

Building EPUB
----------------------------

::

    make clean
    make epub BOOK_LANGUAGE=ru

    epubcheck _build/epub/sphinx.epub
    sigil _build/epub/sphinx.epub


Building HTML
----------------------------

::

    make clean
    git restore _static
    make html BOOK_LANGUAGE=ru


-----

Reading Epub3 with diacritics
================================

iOS (iPhone и iPad):
   Apple Books

Android:
   Google Books

PC:
   Chrome browser with extensions: "Readium" or "EPUB Reader"

----


.local/lib/python3.8/site-packages/sphinx/writers/texinfo.py
 
 ```
  def visit_Text
```

.local/lib/python3.8/site-packages/sphinx/writers/latex.py
 
```
    def visit_attribution(self, node: Element) -> None:
        self.body.append(CR + r'\begin{flushright}' + CR)
        self.body.append('(')

    def depart_attribution(self, node: Element) -> None:
        self.body.append(')')
        self.body.append(CR + r'\end{flushright}' + CR)
```

.local/lib/python3.8/site-packages/sphinx/util/texescape.py

 # A map to avoid TeX ligatures or character replacements in PDF output

 # xelatex/lualatex/uplatex are handled differently (#5790, #6888)

 ascii_tex_replacements = [


