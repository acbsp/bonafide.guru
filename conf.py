# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import argparse
import os
import sys
sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'Истинный гуру'
copyright = '2022, Abhay Charan das'
author = 'Йагйасена прабху'

# The full version, including alpha/beta/rc tags
release = '2022.01.07'

show_authors = True

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
#extensions =  []
extensions = ['sphinx.ext.mathjax']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'ru'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# Enable figures numbering
numfig = True

# Date format if `today` not set
today_fmt = "%Y-%m-%d"

# PDF build from the LaTeX files created by Sphinx will use xindy (doc) rather than makeindex for preparing the index of general terms (from index usage). 
latex_use_xindy = True

text_add_secnumbers = False


latex_engine = 'xelatex'

# Grouping the document tree into LaTeX files. List of tuples# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
 ('index', 'bonafide.guru.tex', u'Истинный гуру', u'Abhay Charan das', 'manual'),
]

latex_elements = {
    # 'passoptionstopackages': r'\usepackage{fancybox}',

    # https://www.sphinx-doc.org/en/master/latex.html
    # The dimensions of the horizontal and vertical margins passed to the geometry package:
    'sphinxsetup': 'hmargin={0.8in,0.4in}, vmargin={0.7in,0.7in}, marginpar=1in',

    # A5 paper size
    "papersize": "a5paper",
    # Oneside pages
    "classoptions": ",twoside",
    # Custom preamble to tune title page
#    "preamble": preamble,
    # The font size ('10pt', '11pt' or '12pt').
    "pointsize": "10pt",

    # https://www.sphinx-doc.org/en/master/latex.html
    'makeindex': '\\usepackage[columns=1]{idxlayout}\\makeindex',
    'printindex': '\\renewcommand{\\indexname}{Указатель цитируемых санскритских стихов}\\small\\raggedright\\printindex',
    # Disable Index page
    #"printindex": "",

    'preamble': r'''

        \usepackage{xltxtra}
        \usepackage{xunicode}

%\setmainlanguage[babelshorthands=true]{russian}
%\setotherlanguage{english}

%\defaultfontfeatures{Ligatures=TeX,Renderer=Basic}
%\setmainfont{Times New Roman}
%\newfontfamily\cyrillicfonttt{Times New Roman}
%\newfontfamily\cyrillicfont{Times New Roman}

%\usepackage{comment}
%\usepackage{float}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% The first part is used for the ebook, 
%  the second part for your PDF file !!
\ifdefined\HCode
 \usepackage[russian]{babel}
 \usepackage[T1]{fontenc}
 \usepackage[utf8]{inputenc}
% \usepackage{tex4ebook}

  \usepackage{alternative4ht}
  \altusepackage{fontspec}
 
 \else

  \usepackage{polyglossia}
  \setdefaultlanguage{russian}
  \setotherlanguages{english}
%\setotherlanguages{english,hindi,sanskrit}
%\newfontfamily\devanagarifont[Script=Devanagari]{Lohit Devanagari}
%\setkeys{russian}{babelshorthands=true}

  \usepackage{fontspec}
  \setmainfont{CharisSIL}[
   Path = /usr/share/fonts/okalash/CharisSIL-6.001/,
   Extension = .ttf,
   UprightFont = *-Regular,
   %-- Upright --%
   FontFace={m}{n}{Font=*-Regular},
   FontFace={b}{n}{Font=*-Bold},
   % %-- Italic --%
   FontFace={m}{it}{Font=*-Italic},
   FontFace={b}{it}{Font=*-BoldItalic},
  ]

  \setromanfont{CharisSIL}
  %\setsansfont{CharisSIL}
  %\setmonofont{CharisSIL}

  \newfontfamily{\cyrillicfont}{CharisSIL}
  \newfontfamily{\cyrillicfontrm}{CharisSIL}
  %\newfontfamily{\cyrillicfonttt}{CharisSIL}
  %\newfontfamily{\cyrillicfontsf}{CharisSIL}


\usepackage{fancyhdr}
\pagestyle{fancy}
\fancyhf{}
\makeatletter
  \fancypagestyle{normal}{
    \fancyhf{}
%    \fancyfoot[LE,RO]{}
%    \fancyfoot[LO]{}
%    \fancyfoot[RE]{}
%    \fancyfoot[C]{\thepage} % except the center  
    \fancyhead[LE,RO]{\thepage}
    \renewcommand{\headrulewidth}{0.1pt}
    \renewcommand{\footrulewidth}{0pt}
  }
\makeatother

\defaultfontfeatures{Scale=MatchLowercase, Mapping=tex-text}

\addtolength{\topmargin}{-.2in}
\addtolength{\textheight}{0.4in}

\input{style.tex.txt}

%\setlength{\parindent}{1.5em} % Paragraph Indentation - By default, LATEX does not indent the first paragraph of a section or a chapter.
%\setlength{\parskip}{0.5em} % Paragraph spacing - determines the space between a paragraph and the preceding text.
%\addtolength{\parskip}{-.3em}
%\renewcommand{\baselinestretch}{1.5} % Line spacing -

\usepackage[titles]{tocloft}
\cftsetpnumwidth {1.25cm}\cftsetrmarg{1.5cm}
\setlength{\cftchapnumwidth}{0.75cm}
\setlength{\cftsecindent}{\cftchapnumwidth}
\setlength{\cftsecnumwidth}{1.25cm}

% Зачем: Отключает использование изменяемых межсловных пробелов.
% Почему: Так не принято делать в текстах на русском языке.
\frenchspacing


% It is my code:
\def\changemargin#1#2{\list{}{\rightmargin#2\leftmargin#1}\item[]}
\let\endchangemargin=\endlist

%   {\thechapter\hsp\textcolor{gray75}
\usepackage{titlesec, blindtext, color}
\definecolor{gray75}{gray}{0.75}
\newcommand{\hsp}{\hspace{20pt}}
%\titleformat{\chapter}
%    [hang]
%    {\Huge\bfseries}
%    {\thechapter\hsp\textcolor{gray75} {|}\hsp}
%    {0pt}
%    {\Huge\bfseries}

%\titleformat{\chapter}
%            [hang]
%            {\huge\bfseries}
%            {
%%        \begingroup
%%        \centering        
%            {\tiny Йагйасена\textendash~Прабхупа̄да дас}
%            {\textcolor{gray75}{|}}
%            {\normalsize Истинный гуру}
%%        \endgroup
%        \hsp\textcolor{gray75}{|}\hsp}
%        {0pt}
%        {\huge\bfseries}
\titleformat{\chapter}[frame]
    {\normalfont\bfseries}
    {\filright
      \normalsize
      \enspace  {\footnotesize Йагйасена \textendash~Прабхупа̄да дас}
                {\hsp\textcolor{gray75}{|}\hsp} 
                {Истинный гуру}  
     \enspace}
    {20pt}
    {\Huge\bfseries\filcenter}

%\titleformat{\section}[runin]
%  {\normalfont\scshape}
%  {}{0pt}{}
%\titlespacing{\section}
%  {\parindent}{*2}{\wordsep}
%\titleformat{\section}
%  {\titlerule
%    \vspace{.8ex}%
%    \normalfont\itshape}
%  {\thesection.}{.5em}{}

%\titleformat{\chapter}[display]
%{\normalfont\huge\bfseries}{\chaptertitlename\ \thechapter}{20pt}{\Huge}
\titleformat{\section}
{\normalfont\Large\bfseries}{\thesection}{1em}{}
\titleformat{\subsection}
{\normalfont\large\bfseries}{\thesubsection}{1em}{}
\titleformat{\subsubsection}
{\normalfont\normalsize\bfseries}{\thesubsubsection}{1em}{}
\titleformat{\paragraph}[runin]
{\normalfont\normalsize\bfseries}{\theparagraph}{1em}{}
\titleformat{\subparagraph}[runin]
{\normalfont\normalsize\bfseries}{\thesubparagraph}{1em}{}

%\titlespacing*{\chapter} {0pt}{50pt}{40pt}
\titlespacing*{\section} {0pt}{3.5ex plus 1ex minus .2ex}{2.3ex plus .2ex}
\titlespacing*{\subsection} {0pt}{3.25ex plus 1ex minus .2ex}{1.5ex plus .2ex}
\titlespacing*{\subsubsection}{0pt}{3.25ex plus 1ex minus .2ex}{1.5ex plus .2ex}
\titlespacing*{\paragraph} {0pt}{3.25ex plus 1ex minus .2ex}{1em}
\titlespacing*{\subparagraph} {\parindent}{3.25ex plus 1ex minus .2ex}{1em}

\fi
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

''',
}

latex_show_urls = 'footnote'

rst_epilog = r"""
.. |noFrameStart| raw:: latex

   \begingroup
   \setlength{\arrayrulewidth}{0pt}

.. |noFrameEnd| raw:: latex

   \endgroup

.. |sub123| replace:: mine123
"""
rst_prolog = """
.. |sub234| replace:: mine234
"""

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

latex_additional_files = [
    "images/logo.png",
    "style.tex.txt",
]

