bibbreviate
===========

A python script to abbreviate journal names in a bib file using publicly available journal lists.

Installation
============

    pip install bibbreviate

or download the source and 

    python setup.py install

Usage
=====

```
usage: bibbrev [-h] [-o OUTPUT] [-r] [-a ABBREVIATIONS] [-v] target

positional arguments:
  target                The bib file to abbreviate.

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        The output file name. If missing, output will be sent
                        to stdout.
  -r, --reverse         Reverse the process and unabbreviate journal names.
  -a ABBREVIATIONS, --abbreviations ABBREVIATIONS
                        Path to a file of abbreviations in the form (one per
                        line): Journal of Biological Science = J. Sci. Biol.
  -v, --verbose
```

WARNING: this package is still in beta.  I use it on my own bib files, but errors are still more than possible.  Be sure to back up your files before using.

Development
===========

The code for this package is hosted on GitHub (https://github.com/Winawer/bibbreviate), and is licensed under the MIT license.  If you have improvements to the package, please submit a pull request and I will be happy to work them in.

 
