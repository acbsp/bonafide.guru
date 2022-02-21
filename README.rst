# bonafide.guru

https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html

https://www.sphinx-doc.org/en/master/usage/configuration.html



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


------------

cat contents.rst |sed -En 's/^[ ]{1,3}\*{1,2}([а-я].*)\*{1,2}$/\1/p' >sed3.txt

cat sed3.txt |sort  >sed3_sorted.txt

cat  sed3_sorted.txt|uniq > sed3_sorted_uniq.txt

cp  sed3_sorted_uniq.txt    sed_RESULT.txt

------------

```
cd ~/Book/bonafide.guru/_build/latex 
xindy -o outfile.ind -L russian -C utf8 -I xelatex -M texindy.xdy  sphinx.idx
```


Способы чтения Epub3.
    iOS
        На мобильных устройствах на базе iOS (iPhone и iPad) файлы в формате EPUB можно читать с помощью «родного» приложения Apple Books.

    Android
        На мобильных устройствах с операционной системой Android книги в формате EPUB можно читать с помощью программ Google Books (обработка книг может занять несколько минут) и др.

    Персональный КОМПЬЮТЕР
        В браузере Chrome файлы EPUB можно читать с расширением Readium или EPUB Reader. В браузере Firefox файлы EPUB можно читать с расширением EPUB Reader. 


```
pip3 install -U sphinx
pip3 install sphinx-rtd-theme
git clone git@github.com:acbsp/bonafide.guru.git
cd bonafide.guru
make clean
make epub BOOK_LANGUAGE=ru

epubcheck _build/epub/sphinx.epub
sigil _build/epub/sphinx.epub


make clean
git restore _static
make html BOOK_LANGUAGE=ru

``` 




===============
 Bona Fide Guru
===============

This project is a tool that makes it easy to create "Bona Fide Guru" book in Russian and English in following output formats:

* PDF 
* HTML
* Epub

It uses `Sphinx`__ engine (4.4.0)

.. __: http://www.sphinx-doc.org/

`reStructuredText` format is used as its markup language.

Installation
============

For Ubuntu distribution

PDF needs TeX Live: XeTeX and packages::

   apt install texlive-xetex texlive-fonts-extra

Install Sphinx and needed dependencies::

   pip install -U sphinx
   pip install sphinx_rtd_theme

Documentation
=============

Documentation is available from `sphinx-doc.org`__.

__ http://www.sphinx-doc.org/

Get in touch
============

- Report bugs, suggest features or view the source code `on GitHub`_.
- For less well defined questions or ideas, use the `mailing list`_.

.. _on GitHub: https://github.com/sphinx-doc/sphinx
.. _mailing list: https://groups.google.com/forum/#!forum/sphinx-users

Please adhere to our `code of conduct`__.

__ http://www.sphinx-doc.org/en/master/code_of_conduct.html

Testing
=======

Continuous testing is provided by `Travis`__ (for unit tests and style checks
on Linux), `AppVeyor`__ (for unit tests on Windows), and `CircleCI`__ (for
large processes like TeX compilation).

For information on running tests locally, refer to `the contributors guide`__.

__ https://travis-ci.org/sphinx-doc/sphinx
__ https://ci.appveyor.com/project/sphinxdoc/sphinx
__ https://circleci.com/gh/sphinx-doc/sphinx
__ http://www.sphinx-doc.org/en/master/internals/contributing.html

Contributing
============

Refer to `the contributors guide`__.

__ http://www.sphinx-doc.org/en/master/internals/contributing.html
