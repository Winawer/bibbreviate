import bibtexparser as bt
from argparse import ArgumentParser

def main():
  parser = ArgumentParser()
  parser.add_argument("target",help="The bib file to abbreviate.")
  parser.add_argument("-o","--output",help="The output file name.  If missing, output will be sent to stdout.")
  args = parser.parse_args()



if __name__ == "__main__":
  main()
