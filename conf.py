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
copyright = '2021, Abhay Charan das'
author = 'Ягья Сена прабху - Прабхупада дас'

# The full version, including alpha/beta/rc tags
release = '2021.04.29'


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



#latex_maketitle = r'''
#\input{style.tex.txt}
#'''
# \\input{{style.tex.txt}}
#%\input{style.tex.txt}
preamble = r'''

% Nimbus Samns L - helvetica clone
%\setmainfont{Nimbus Sans L}

% Header and footer
%\pagestyle{fancy}

% Table of Contents
% ToC: depth
%\setcounter{secnumdepth}{4}
...
'''

latex_engine = 'xelatex'
#latex_engine = 'lualatex'


#'fontenc': '\usepackage[T1,T2A]{fontenc}',
#'babel': '\\usepackage[russian]{babel}',
#'cmappkg': '\\usepackage{cmap}',
#'utf8extra':'\\DeclareUnicodeCharacter{00A0}{\\nobreakspace}',
#        \PassOptionsToPackage{hmargin=1in,vmargin=1in,marginpar=0.5in}{geometry}
#        'sphinxsetup': 'hmargin={2in,1.5in}, vmargin={1.5in,2in}, marginpar=1in',
latex_elements = {

#    'passoptionstopackages': r'\usepackage{fancybox}',

# The dimensions of the horizontal and vertical margins passed to the geometry package:
'sphinxsetup': 'hmargin={0.8in,0.4in}, vmargin={0.7in,0.7in}, marginpar=1in',

    # A5 paper size
    "papersize": "a5paper",
    # Oneside pages
    #"classoptions": ",twoside",
    # Custom preamble to tune title page
#    "preamble": preamble,
    # The font size ('10pt', '11pt' or '12pt').
    #"pointsize": "10pt",
    # Disable Index page
    #"printindex": "",
    #'babel': '\\usepackage{babel}',
    #'inputenc': '\\usepackage[utf8]{inputenc}',
    #'cmap': '\\usepackage{cmap}',
    #'fontenc': '\\usepackage[X2,T1]{fontenc}',
#   'maketitle': latex_maketitle,

#\passoptionstopackages{options}{fancybox}
#    'preamble': r'''
#\usepackage[titles]{tocloft}
#\cftsetpnumwidth {1.25cm}\cftsetrmarg{1.5cm}
#\setlength{\cftchapnumwidth}{0.75cm}
#\setlength{\cftsecindent}{\cftchapnumwidth}
#\setlength{\cftsecnumwidth}{1.25cm}
#''',

#'preamble': '\\usepackage[UTF8]{ctex}\n',

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


%\setlength{\parindent}{1.5em} % Paragraph Indentation - By default, LATEX does not indent the first paragraph of a section or a chapter.
%\setlength{\parskip}{0.5em} % Paragraph spacing - determines the space between a paragraph and the preceding text.
%\addtolength{\parskip}{-.3em}
%\renewcommand{\baselinestretch}{1.5} % Line spacing -

\usepackage[titles]{tocloft}
\cftsetpnumwidth {1.25cm}\cftsetrmarg{1.5cm}
\setlength{\cftchapnumwidth}{0.75cm}
\setlength{\cftsecindent}{\cftchapnumwidth}
\setlength{\cftsecnumwidth}{1.25cm}

\input{style.tex.txt}

% Зачем: Делает результирующий PDF "searchable and copyable".
%\usepackage{cmap}


% Зачем: Отключает использование изменяемых межсловных пробелов.
% Почему: Так не принято делать в текстах на русском языке.
\frenchspacing


% It is my code:
\def\changemargin#1#2{\list{}{\rightmargin#2\leftmargin#1}\item[]}
\let\endchangemargin=\endlist

\fi

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

''',


'fncychap': r'\usepackage[Rejne]{fncychap}',
#'fncychap': r'\usepackage[Bjornstrup]{fncychap}', Sonny, Lenny”, “Glenn”, “Conny”, “Rejne”
'printindex': r'\footnotesize\raggedright\printindex',
}
#    'fontenc': '\\usepackage[X2,T1]{fontenc}',

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

