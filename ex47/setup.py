try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description' : 'Learning how to run simple tests',
    'author' : 'Stephen Borutta',
    'url' : 'URL to get it all at',
    'download_url' : 'Where to download it',
    'author_email' : 'boruttasp@gmail.com',
    'version' : '0.1', #major.minor[.patch[.sub]]
    'install_requires' : ['nose'],
    'packages' : ['NAME'],
    'scripts' : [],
    'name' : 'ex47'
}

setup(**config)
