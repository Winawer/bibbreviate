from setuptools import setup, find_packages

files = ["journal_files/*"]

setup(name = "bibbreviate",
      version = "0.0.1",
      description = "Abbreviate journal titles in BibTex files.",
      author = "Steven Hamblin",
      author_email = "steven.hamblin@gmail.com",
      url = "https://github.com/Winawer/bibbreviate",
      packages = find_packages(exclude="tests"),
      package_data = {'src':['journal_files/*.txt']},
      #include_package_data = True,
      #package_data = {'':['*.txt']},
      #packages = find_packages('src'),
      #package_dir = {'': 'src'},
      install_requires = ['setuptools','bibtexparser'],
      entry_points = { 'console_scripts' : ['bibbrev = src.bibbrev:main'] },
      #      entry_points = """
      #[console_scripts]
      #bibbreviate = bibbrev:main
      #""",
      classifiers = [
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Topic :: Text Processing :: Markup :: LaTeX',
        ],
)

