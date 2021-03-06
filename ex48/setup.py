try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description' : 'Making Sentences',
    'author' : 'Stephen Borutta',
    'url' : 'https://github.com/SteviBee/Learn-Python-The-Hard-Way/tree/master/ex48',
    'download_url' : 'Where to download it',
    'author_email' : 'boruttasp@gmail.com',
    'version' : '0.1', #major.minor[.patch[.sub]]
    'install_requires' : ['nose'],
    'packages' : ['NAME'],
    'scripts' : [],
    'name' : 'lexicon'
}

setup(**config)
