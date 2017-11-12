## Nose Definition/About
Nose is a python unit test framework which extends unittest to make testing easier. It collects tests from unitest.TestCase as well as some others not in unitest. A lot of good information [here](http://pythontesting.net/framework/nose/nose-introduction/) and [here](http://nose.readthedocs.io/en/latest/) and
[here](http://ivory.idyll.org/articles/nose-intro.html)


#### Other useful tests to learn are  doctest, unittest, and pytest:

-The doctest module searches for pieces of text that look like interactive Python sessions in docstrings, and then executes those sessions to verify that they work exactly as shown.

-Unittest is the batteries-included test module in the Python standard library.

-py.test is a no-boilerplate alternative to Python’s standard unittest module.

##### Nose Basic Commands


nosetests general script:

`nosetests [options] [(optional) test files or directories]`

Specify a test:

`nosetests a.test:TestCase.test_method`

Testing in script
`import nose
nose.main()`
`import nose
result = nose.run()`

Runs nose test inside current folder:

`PS C:\> python -m nose`

Setup and teardown will be ran via the test runner every time as long as they are in your test file. Lots of times the test file is in the same directory as the main file.

Nosetests command will find:
-files or folder containing 'test' or 'Test' in their name, ex: model_test.py
-functions or classes within these files with 'test' or 'Test' in their name, and they will be ran as tests. Ex: test_function inside model_test.py.

To see exactly what is being tested use verbose:

`PS C:\> python -m nose -v`
