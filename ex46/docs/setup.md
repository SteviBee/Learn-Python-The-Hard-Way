## Setup Definition/About
The setup script is the center of all activity building, distributing, and installing modules using the distutils.

More info [here](https://docs.python.org/3/distutils/setupscript.html)
and get commands [here](https://pythonhosted.org/an_example_pypi_project/setuptools.html)

See 'Setup.py' for typical layout in addition you might need to call the following:

```python
1. setup.py daily bdist_egg        # generate a daily-build .egg file
2. setup.py daily sdist            # generate a daily-build source distro
3. python setup.py bdist_wininst   # creates an exe file
```
But it should work find without it.
