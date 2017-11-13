## Nose Definition/About
Nose is a python unit test framework which extends unittest to make testing easier. It collects tests from unitest.TestCase as well as some others not in unitest. A lot of good information [here](http://pythontesting.net/framework/nose/nose-introduction/) and [here](http://nose.readthedocs.io/en/latest/) and
[here](http://ivory.idyll.org/articles/nose-intro.html)


#### Other useful tests to learn are  doctest, unittest, and pytest:

- The doctest module searches for pieces of text that look like interactive Python sessions in docstrings, and then executes those sessions to verify that they work exactly as shown.

- Unittest is the batteries-included test module in the Python standard library.

- py.test is a no-boilerplate alternative to Python’s standard unittest module.

##### Nose Basic Commands


nosetests general script:

`nosetests [options] [(optional) test files or directories]`

Specify a test:

`nosetests a.test:TestCase.test_method`

Testing in script:

`import nose
nose.main()`

`import nose
result = nose.run()`

Runs nose test inside current folder:

`PS C:\> nosetests`

To see exactly what is being tested use verbose:

`PS C:\> nose -v`

##### Nose Usage
Nose will automatically collect tests from python source files, directories, and packages found in the **working directory** as long as they match the testMatch regular expression, by default:

'?:\b\_)[Tt]est' will be collected

Nosetests will find:

- files or folder containing 'test' or 'Test' in their name, ex: model_test.py

- functions or classes within these files with 'test' or 'Test' in their name, and they will be ran as tests. Ex: test_function inside model_test.py

- From the working directory on down, so module.test, module.sub.test, and module.sub1.sub2.test will all be ran if test ran at top level.

- Does **not** include tests from files which are executable (.exe, .bin, .app, etc) or use `python -m nose --exe` to have nose look into these files. Except windows does.

##### Nose Fixtures

- setup and teardown will be ran via the test runner every time as long as they are in your test directory. These functions must be written in your `__init__.py` of a test package to run, and should be named 'setup' or 'teardown'.

- Setup runs before any test and teardown runs if setup is completed.

##### Test Packages

- Lots of times the test directory is in the same directory as the main directory. That being said you can just write one `test.py` file and keep it in the same place as your package, but generally tests are more robust than one file.

- test directories can be made in same directory as main. Ex: path/project/new/main.py with test path/project/new/test_main.py

- directories that don't look like tests are not inspected.

- packages are always inspected but only collected if tests.
