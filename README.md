**Magento2 test suite**


**About this Test Suite** [About this Test Suite](#about-this-test-suite)

This test suite performs end-to-end functional testing for Magento2 web store, which is running locally on your machine.

Now, let's look how to get things up and running to use the tests.


For SeleniumBase CLI commands, log saving, configurations etc, please have a look at https://github.com/seleniumbase/SeleniumBase.

**[Magento installation](#magento-installation)**

First, install MAGENTO 2 locally using Docker. Via this link you will find necessary instructions.

https://github.com/markshust/docker-magento

```
Note, this setup assumes you are running Docker on a computer with at least 4GB of allocated RAM, a dual-core, and an SSD hard drive. Download & Install Docker Desktop.

This configuration has been tested on Mac & Linux. Windows is supported through the use of Docker on WSL.

```
For reference, you can have a look at a demo website (http://demo.magento-elastic-suite.io/index.php), similar to the one I tested, however page elements there differ, so my tests will fail when running against it.

**SeleniumBase installation**   

Then, install SeleniumBase, an all-in-one framework for web automation, end-to-end testing, and website tours, which I use in this test suite.

Installation:

https://github.com/seleniumbase/SeleniumBase#-get-started

Here is a list of SeleniumBase methods you might find in tests:

https://github.com/seleniumbase/SeleniumBase/blob/master/seleniumbase/fixtures/base_case.py

**Project content**

The project consists of two main parts: test suites and page object files.

```
* Test suites:
mag_test.py
mag_test_search.py

* Page object files:
mag_object
mag_object_catalog
mag_object_cart
mag_object_checkout

```

**To run the tests:**

`$ git clone https://github.com/kate-tel/magento2.test.git <your_directory_name>`

`$ cd <your_directory_name>`

Activate virtual environment to run tests:

`$ source /Users/kate/.virtualenvs/seleniumbase_venv/bin/activate`

Now simply run tests:

`$ pytest magento/mag_test_search.py`

To select a specific test method to run, indicate class name and then method name:

`$ pytest magento/mag_test.py::MagentoTestClass::test_search_fail`

Alternatively, you can specify a test to run, using pytest markers. Each test has its own marker for this purpose.

Running a specific test:

`$ pytest magento/mag_test.py -m=minicart`

Sometimes page load duration is unstable, so in case of **ElementNotVisibleException**, running the test(-s) with a custom settings file will help. In this file timeouts are extended, compared to the default ones. If needed, you can modify the timeouts manually in custom_settings.py.

Running a test with custom settings:

`$ pytest magento/mag_test.py -m=search --settings_file=custom_settings.py`


For other options, log saving, configurations etc, please have a look at https://github.com/seleniumbase/SeleniumBase.


Hope, you enjoy!
