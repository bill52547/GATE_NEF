from setuptools import setup, find_packages

setup(name = 'dbnef',
      version = '0.2.0',
      py_modules = ['gatenef'],
      description = 'GATE TOOLBOX NEF',
      author = 'Minghao Guo',
      author_email = 'mh.guo0111@gmail.com',
      license = 'Apache',
      packages = find_packages(),
      install_requires = [
          'sqlalchemy'],
      zip_safe = False,
      entry_points = '''

      ''',
      )
