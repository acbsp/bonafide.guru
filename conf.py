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

project = 'Истинный Гуру'
copyright = '2022, Abhay Charan das'
author = 'Ягьясена -- Прабхупа̄да дас'

# The full version, including alpha/beta/rc tags
release = '2022.01.22'

show_authors = False
smartquotes = True

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
# ('index', 'bonafide.guru.tex', u'Истинный Гуру', u'Abhay Charan das', 'manual'),
# ('index', 'bonafide.guru.tex', 'Истинный Гуру', 'Abhay Charan das', 'manual', False),
latex_documents = [
 ('index', 'bonafide.guru.tex', u'Истинный Гуру', u'Ягьясена -- Прабхупа̄да дас', 'manual', False),
]

latex_elements = {
    # 'passoptionstopackages': r'\usepackage{fancybox}',
    #'passoptionstopackages': r'\usepackage[pdfusetitle,hidelinks,unicode]{hyperref}',
    #'passoptionstopackages': r'\usepackage[pdfusetitle,unicode,xetex,bookmarks=true,colorlinks=true,linkcolor=headernfooter,urlcolor=headernfooter,linktoc=section,]{hyperref}',
    #'passoptionstopackages': r'\usepackage[%draft=true,pdfa=true,bookmarks=true,bookmarksopen=true,bookmarksopenlevel=1,unicode=true,pdfauthor={My Name},pdftitle={My Title}, breaklinks,hidelinks,colorlinks=true,linkcolor=blue,citecolor=blue,urlcolor=blue]{hyperref}',
    'passoptionstopackages': r'\usepackage[pdfa=true,dvipdfmx-outline-open,bookmarks=true,bookmarksopen=true,bookmarksopenlevel=2,unicode=true,pdfusetitle=true,hidelinks=true,pdfkeywords={Гаўдӣйа-Ваишн̣авизм,ISKCON,Международное Общество для Осознания Кришны, Его Божественная Милость Ш́рӣ Ш́рӣмад А.Ч. Бхактиведанта Свами Прабхупа̄да,Дӣкша̄-гуру},pdfsubject={подношение лотосным стопам нашего возлюбленного духовного учителя, к 110-летию божественного явления Основателя-А̄ча̄рйи ISKCON},]{hyperref}',

    # https://www.sphinx-doc.org/en/master/latex.html
    # The dimensions of the horizontal and vertical margins passed to the geometry package:
    # Default: 1in,1in,0.5in
    #'sphinxsetup': 'hmargin={0.8in,0.4in}, vmargin={0.7in,0.7in}, marginpar=1in',
    'sphinxsetup': 'hmargin={0.5in,0.5in}, vmargin={0.5in,0.5in}',

    # A5 paper size
    "papersize": "a5paper",
    # Oneside pages
    #"classoptions": ",twoside",
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

    \setlength{\headheight}{0.5in}
    \addtolength{\topmargin}{-0.2in}
    % A similar change would be necessary for \footskip 
    % if the footer comes out too tall:
    %   \footskip 

    \usepackage{fourier-orns}
    \usepackage{pgfornament}

%\addtolength{\topmargin}{-.2in}
%\addtolength{\textheight}{0.4in}

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
  %\setmainfont{Times New Roman}
  %\newfontfamily\cyrillicfont{Times New Roman}

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

  %\newfontface\tnrfam[Scale=MatchUppercase]{FreeSerifBold}
  \newfontface\tnrfam{Times New Roman}
  \newfontface\tnrItalicfam{Times New Roman Italic}
  \newfontface\tnrBoldfam{Times New Roman Bold}
  \newfontface\tnrBIfam{Times New Roman Bold Italic}
  \newcommand*\BonafideGuru{%
    {\tnrBoldfam Истинный Гуру}%
  }%
  \newcommand*\BonafideGuruN{%
    {\tnrfam Истинный Гуру}%
  }%
  \newcommand*\Yagyasena{%
    {\cyrillicfont Ягьясена \textendash~Прабхупа̄да дас}%
  }%

  \newcommand\decorCenterRuler{%
        \hrulefill
        \raisebox{-2.1pt}
        {\quad\decofourleft\decotwo\decofourright\quad}%
        \hrulefill}
  \newcommand\decorCenter{%
        \strut\hfill
        \raisebox{-2.1pt}
        {\quad\decofourleft\decotwo\decofourright\quad}%
        \hfill\strut}
   \newcommand\myoldpilcrowfour{%
           \noindent {\oldpilcrowfour}\,}
   \newcommand\myoldpilcrowfive{%
           \noindent {\oldpilcrowfive}\,}
   \newcommand\myoldpilcrowsix{%
           \noindent {\oldpilcrowsix}\,}

\usepackage{eso-pic}
\newcommand\AtPageUpperRight[1]{\AtPageUpperLeft{%
 \put(\LenToUnit{\paperwidth},\LenToUnit{0\paperheight}){#1}%
 }}%
\newcommand\AtPageLowerRight[1]{\AtPageLowerLeft{%
 \put(\LenToUnit{\paperwidth},\LenToUnit{0\paperheight}){#1}%
 }}%
\newcommand{\beautify}{%
 \AddToShipoutPictureBG{%
   \AtPageUpperLeft{\put(0,-25){\pgfornament[width=1.75cm]{61}}}
   \AtPageUpperRight{\put(-50,-25){\pgfornament[width=1.75cm,symmetry=v]{61}}}
   \AtPageLowerLeft{\put(0,25){\pgfornament[width=1.75cm,symmetry=h]{61}}}
   \AtPageLowerRight{\put(-50,25){\pgfornament[width=1.75cm,symmetry=c]{61}}}
   }
   }

\newcommand{\simplify}{%
     \cleardoublepage\ClearShipoutPictureBG
     %\ClearShipoutPictureBG
   }

\usepackage{fancyhdr}
\pagestyle{fancy}
\fancyhf{}
\makeatletter
  \fancypagestyle{normal}{
    \fancyhf{}
%%    \fancyfoot[LE,RO]{}
%%    \fancyfoot[LO]{}
%%    \fancyfoot[RE]{}
%%    \fancyfoot[C]{\thepage} % except the center  
%%    \fancyhead[LE,RO]{\thepage}
%%    \fancyfoot[C]{\textbf{--~\thepage~--}} % except the center
    \renewcommand{\headrulewidth}{0pt}
    \renewcommand{\footrulewidth}{0pt}
    \renewcommand{\headrule}{} % disappear
    \renewcommand{\footrule}{} % disappear
    \fancyhead[LE,RO]{\textbf{\thepage}}
%    \renewcommand\footrule{%
%        \hrulefill
%        \raisebox{-2.1pt}
%        {\quad\decofourleft\decotwo\decofourright\quad}%
%        \hrulefill}
  }
  \fancypagestyle{plain}{%
    \fancyhf{}% clear all header and footer fields
%    \fancyfoot[C]{\textbf{--~\thepage~--}} % except the center
    \renewcommand{\headrulewidth}{0pt}%
    \renewcommand{\footrulewidth}{0pt}%
  }
\makeatother

%\defaultfontfeatures{Scale=MatchLowercase, Mapping=tex-text}

\input{style.tex.txt}

%\setlength{\parindent}{1.5em} % Paragraph Indentation - By default, LATEX does not indent the first paragraph of a section or a chapter.
%\setlength{\parskip}{0.5em} % Paragraph spacing - determines the space between a paragraph and the preceding text.
%\addtolength{\parskip}{-.3em}
%\renewcommand{\baselinestretch}{1.5} % Line spacing -

%\usepackage[titles]{tocloft}
%\cftsetpnumwidth {1.25cm}\cftsetrmarg{1.5cm}
%\setlength{\cftchapnumwidth}{0.75cm}
%\setlength{\cftsecindent}{\cftchapnumwidth}
%\setlength{\cftsecnumwidth}{1.25cm}

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
%            {\tiny Ягьясена\textendash~Прабхупа̄да дас}
%            {\textcolor{gray75}{|}}
%            {\normalsize Истинный Гуру}
%%        \endgroup
%        \hsp\textcolor{gray75}{|}\hsp}
%        {0pt}
%        {\huge\bfseries}

% With Author and Book names:
%\titleformat{\chapter}[frame]
%    {\normalfont\bfseries}
%    {\filright
%      \normalsize
%      \enspace  {\footnotesize Ягьясена \textendash~Прабхупа̄да дас}
%                {\hsp\textcolor{gray75}{|}\hsp} 
%                {Истинный Гуру}  
%     \enspace}
%    {20pt}
%    {\Huge\bfseries\filcenter}

\titleformat{\chapter}[frame]
    {\normalfont\bfseries}
    {}
    {8pt}
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
    "images/_july9th.jpg",
    "images/_will1.jpg",
    "images/_will2.jpg",
    "style.tex.txt",
]

