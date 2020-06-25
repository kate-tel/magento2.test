**Magento2 test suite**

**About this Test Suite**

This test suite perfoms end-to-end functional testing for Magento2 web store, running locally on your machine.

Now, let's look how to get things up and running to simply run the tests from this repo.

**Magento installation**

First, install MAGENTO 2 locally using Docker. Via this link you will find necessary instructions.

https://github.com/markshust/docker-magento

Note, this setup assumes you are running Docker on a computer with at least 4GB of allocated RAM, a dual-core, and an SSD hard drive. Download & Install Docker Desktop.

This configuration has been tested on Mac & Linux. Windows is supported through the use of Docker on WSL.

**SeleniumBase installation**   

Then, install SeleniumBase, an all-in-one framework for web automation, end-to-end testing, and website tours, which I use in this test-suite.

Installation:

https://github.com/seleniumbase/SeleniumBase#-get-started

**To run the tests:**

`$ git clone https://github.com/kate-tel/magento2.test.git <your_directory_name>`

`$ cd <your_directory_name>`

To activate virtual environment to run tests:

`$ source /Users/kate/.virtualenvs/seleniumbase_venv/bin/activate`

Now simply run tests:

`$ pytest magento/mag_test_search.py`

To select a specific test method to run, indicate class name and then method name:

`$ pytest magento/mag_test.py::MagentoTestClass::test_search_fail`

Hope, you enjoy!
