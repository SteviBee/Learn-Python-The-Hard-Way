## Virtualenv Definition/About
It is an isolated working copy of python which allows me to work on specific projects without affecting other projects.

It solves the problem of dependencies, versions, and somewhat permissions. It installs packages in separate locations, E.g. not globally in `user\lib\python2.7\site-packages`, and creates a lib, include, scripts, and tcl directories.

- **Lib** - installs the site-packages and other library files for a new virtual environment in python.
- **include** - similar to lib because it installs file needed for the new environment.
- **scripts** - (or bin) where executables live. Notably the new python.exe file, but also all the package's executables.
- **tcl** - Tool Command Language. It is used to allow programs to interact with other programs and as an embeddable interpreter. More info [here](https://www.tutorialspoint.com/tcl-tk/tcl_overview.htm)


Good documents to read [offical](https://virtualenv.pypa.io/en/stable/), [here](http://docs.python-guide.org/en/latest/dev/virtualenvs/), and more [basic](http://www.pythonforbeginners.com/basics/how-to-use-python-virtualenv). If you want to go the absolute path look [here](http://www.pfinn.net/install-pip-virtualenv-on-windows.html)

##### Basic Commands

1. Create a new environment:

`PS C:\> virtualenv Project_Directory_Name`

will install the three directories above, as well as pip, setuptools, and wheel in order for you to start installing packages.

2. Activate Environment:

`PS C:\path\to\Project_Directory_Name\Scripts\activate.ps1`

`(Project_Directory_Name) PS C:\path\to\Project_Directory_Name\Scripts\>`

Will activate the virtual environment (you might have to override some security parameters see [offical](https://virtualenv.pypa.io/en/stable/)). The virtual environment will be displayed to the right. Now everything you do is going to stay in this directory & packages installed in this Lib.

3. Deactivate Environment:

`PS C:\> virtualenv deactivate`

Will take you back to using your global packages.

##### Note

It is good practice to freeze your current state so you can come back to it via (in your VirEnv or not):

``PS C:\> pip freeze > requirements.txt`
