from setuptools import setup, find_packages

files = ["journal_files/*"]

readme = open('README.md','r')
README_TEXT = readme.read()
readme.close()

setup(name = "bibbreviate",
      version = "0.1",
      description = "Abbreviate journal titles in BibTex files.",
      long_description = README_TEXT,
      author = "Steven Hamblin",
      author_email = "steven.hamblin@gmail.com",
      url = "https://github.com/Winawer/bibbreviate",
      packages = find_packages(exclude="tests"),
      package_data = {'src':['journal_files/*.txt']},
      install_requires = ['setuptools','bibtexparser'],
      entry_points = { 'console_scripts' : ['bibbrev = src.bibbrev:main'] },
      classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Topic :: Text Processing :: Markup :: LaTeX',
        ],
)

