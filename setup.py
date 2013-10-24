from distutils.core import setup
setup(name = 'movespy',
      version = '0.1.3',
      
      
      author = 'Eric S. Talbot',
      maintainer = 'Eric S. Talbot',
      url = 'http://ericstalbot.github.com/movespy',
      description = 'Easy Python tools for EPA MOVES project-level analysis',
      long_description = open('README.txt').read(),


      packages = ['movespy'],
      requires = ['numpy','MySQLdb'])
