from bibtexparser.bparser import BibTexParser
from bibtexparser.customization import homogeneize_latex_encoding
from bibtexparser.bwriter import to_bibtex
from argparse import ArgumentParser
import os,sys,codecs,logging,re

logging.basicConfig()
logger = logging.getLogger('bibbreviate')

#TODO implement a best guess pass, based on the 'rules' of abbreviation.
#TODO create a utility to update the journal list
def determine_path ():
    """Borrowed from wxglade.py"""
    try:
        root = __file__
        if os.path.islink (root):
            root = os.path.realpath (root)
        return os.path.dirname (os.path.abspath (root))
    except:
        print "I'm sorry, but something is wrong."
        print "There is no __file__ variable. Please contact the author."
        sys.exit ()
        


def load_abbrevs(fn,reverse=False):
  # This load trick from http://stackoverflow.com/questions/4842057/python-easiest-way-to-ignore-blank-lines-when-reading-a-file
  abbrevs = filter(None,(line.rstrip() for line in codecs.open(fn,encoding='utf-8')))
  abbrevs = [ line.split('=') for line in abbrevs ]
  abbrevs = [ [line[0].strip(),line[1].strip()] for line in abbrevs ]
  if not reverse:
    abbrevs = { line[0].strip().lower():line[1].strip() for line in abbrevs}
  else:
    abbrevs = { line[1].strip().lower():line[0].strip() for line in abbrevs}
  return abbrevs

def main():
  parser = ArgumentParser()
  parser.add_argument("target",help="The bib file to abbreviate.")
  parser.add_argument("-o","--output",help="The output file name.  If missing, output will be sent to stdout.")
  parser.add_argument("-r","--reverse",help="Reverse the process and unabbreviate journal names.",action="store_true")
  parser.add_argument("-a","--abbreviations",help="Path to a file of abbreviations in the form (one per line): Journal of Biological Science = J. Sci. Biol.")
  parser.add_argument("-v","--verbose",action="store_true")

  args = parser.parse_args()

  level = logging.WARNING if not args.verbose else logging.INFO
  logger.setLevel(level)

  input = open(args.target,"r")
  output = open(args.output,"w") if args.output else sys.stdout

  refs_bp = BibTexParser(input.read(),customization=homogeneize_latex_encoding)
  refs = refs_bp.get_entry_dict()
  abbrevs = load_abbrevs(determine_path()+"/journal_files/journal_abbreviations_general.txt",reverse=args.reverse)

  for ref in refs:
    if 'journal' in refs[ref]:
      # Assume that if it has a journal key, then it needs abbreviating.  I'm doing this
      # instead of testing for type==article in case I've forgotten about a case where
      # type != article but there's a journal field.
      # Also, journal names with one word ('Nature') don't require abbreviation.
      if len(refs[ref]['journal'].split(' ')) > 1:
        journal = refs[ref]['journal'].lower()

        # Handle any difficult characters.  TODO: check that this list is complete.
        journal_clean = re.sub('[{}]','',journal)

        try:
          refs[ref]['journal'] = abbrevs[journal_clean]
          logger.info('%s replaced with %s for key %s' % (journal,abbrevs[journal_clean],ref))
        except KeyError:
          logger.error('%s not found in abbreviations!' % (journal_clean))

  output_bib = to_bibtex(refs_bp)
  output.write(output_bib)

if __name__ == "__main__":
  main()
