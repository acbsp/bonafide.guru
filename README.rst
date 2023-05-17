===============
 Bona Fide Guru
===============

This project is a tool that makes it easy to create "Bona Fide Guru" book with diacritic signs in following output formats:

* PDF 
* HTML
* Epub

in Russian and English using free software and fonts.

It uses `Sphinx`__ engine (4.4.0), `LaTeX`__ for creating PDF, 'reStructuredText' format as its markup language.

.. __: http://www.sphinx-doc.org/
.. __: https://www.tug.org/texlive/

"`CharisSIL`__" family of fonts is used for printing to web and mobile. It supports advanced OpenType features useful for multilingual texts, including careful diacritic positioning.

.. __: https://software.sil.org/charis/


Installation (Ubuntu GNU/Linux distribution)
=============================================

Install Sphinx and needed dependencies::

   apt install sphinx sphinx_rtd_theme
   apt install cmake bash sed git

PDF needs TeX Live (XeTeX and font packages)::

   apt install texlive-xetex texlive-fonts-extra

Building book
============================

Get sources
----------------------------

::

  git clone git@github.com:acbsp/bonafide.guru.git
  cd bonafide.guru

Building PDF (English)
----------------------------

::

    make clean BOOK_LANGUAGE=en
    make latexpdf BOOK_LANGUAGE=en

Building EPUB (English)
----------------------------

::

    make clean BOOK_LANGUAGE=en
    make epub BOOK_LANGUAGE=en

    epubcheck _build/epub/sphinx.epub
    sigil _build/epub/sphinx.epub


Building HTML (English)
----------------------------

::

    make clean BOOK_LANGUAGE=en
    make html BOOK_LANGUAGE=en


Building Russian book
----------------------------

Change language by using::

    BOOK_LANGUAGE=ru

in command.

Reading Epub3 with diacritic
================================

iOS (iPhone и iPad):
   Apple Books

Android:
   Google Books

PC:
   Chrome browser with extensions: "Readium" or "EPUB Reader"


PDF: Fix to have `()` as quote signature instead of `--`
==========================================================

It needs to find your local Sphinx file `latex.py` in /writers/ directory and fix it manually:

(mine was at .local/lib/python3.8/site-packages/sphinx/writers/latex.py)
 
::

    def visit_attribution(self, node: Element) -> None:
        self.body.append(CR + r'\begin{flushright}' + CR)
        self.body.append('(')

    def depart_attribution(self, node: Element) -> None:
        self.body.append(')')
        self.body.append(CR + r'\end{flushright}' + CR)



