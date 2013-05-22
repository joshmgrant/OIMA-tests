OIMA-tests
==========

Some functional tests for the Ontario Independent Music Archive. 

Currently this only has basic tests, and is written in Python for use with py.test.

To run these tests:

1. Install py.test on your preferred OS. See http://pytest.org/latest/getting-started.html

If you have not used py.test before, take a look at some examples of how it is used: http://pytest.org/latest/getting-started.html#our-first-test-run

2. Make sure you have the correct browsers installed for use. Firefox is generally the easiest browser to use, but tests can be configured for Chrome as well.

3. Select a test script to run. These scripts generally have the term "test" in the file name, eg browsetest.py.

4. Run this script as a py.test script at the command prompt eg run "py.test browsetest.py". 

5. Watch the browsers start up and run.

6. Interpret results. Good testing!