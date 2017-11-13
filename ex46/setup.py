from os.path import join as pjoin

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description' : 'My Project',
    'author' : 'Stephen Borutta',
    'url' : 'https://github.com/SteviBee/Learn-Python-The-Hard-Way/tree/master/ex46',
    'download_url' : 'https://github.com/SteviBee/Learn-Python-The-Hard-Way/tree/master/ex46',
    'author_email' : 'boruttasp@gmail.com',
    'version' : '0.1',
    'install_requires' : ['nose'],
    'packages' : ['ex46'],
    'scripts' : [pjoin('bin','say_hello')],
    'name' : 'ex46'
}

setup(**config)
