Follow these general loose set of guidelines when making your tests: (From Learn-Python-The-Hard-Way ex47)

1. Test files go in tests/ and are named BLAH_tests.py otherwise nosetests won't run them. This also keeps
your tests from clashing with your other code.

2. Write one test file for each module you make.

3. Keep your test cases (functions) short, but do not worry if they are a bit messy. Test cases are usually kind of
messy.

4. Even though test cases are messy, try to keep them clean and remove any repetitive code you can. Create helper
functions that get rid of duplicate code. You will thank me later when you make a change and then have to
change your tests. Duplicated code will make changing your tests more difficult.

5. Finally, do not get too attached to your tests. Sometimes, the best way to redesign something is to just delete it,
the tests, and start over
