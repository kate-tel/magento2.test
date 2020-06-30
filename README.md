## **Magento 2 End-to-end-testing**

### **Table of Contents**

* [About this Project](#about-this-project)
* [Test coverage](#test-coverage)
* [Prerequisites](#prerequisites)
* [Magento installation](#magento-installation)
* [Configuring Catalog Search](#configuring-catalog-search)
* [Setup of testing environment](#setup-of-testing-environment)
* [Running the tests](#running-the-tests)
* [Project content](#project-content)
* [References](#references)

### **About this Project**

This test suite performs end-to-end functional testing for a local demo [Magento 2 web store](https://magento.com/).

### **Test coverage**

Functionality covered by this test suite:

* Website search and search suggestions;
* Addding and manipulating items in comparison list;
* Adding and manipulating items in wish list;
* Adding and manipulating items in cart;
* Adding and manipulating items in minicart;
* Checkout by a registered user;
* Checkout by a guest;
* Login;
* Account creation.

Functionality not covered:

* Payment method choice. *
* Order cancellation; *
* Order amendment;    *
* Password reset; *
* Account Deletion;
* Editing account;
* Contact form Submission;
* Orders and Returns form Submission;
* Advanced search;
* Newsletter subscription;    *
* Review submission;

Functionalities marked with * need additional configuartion to be tested.

### **Prerequisites**

You should have the following installed:

* [Python 3](https://www.python.org/downloads/)
* [Docker Desktop](https://www.docker.com/products/docker-desktop)
* [Elasticsearch 7.8.0](https://www.elastic.co/guide/en/elasticsearch/reference/current/getting-started-install.html#run-elasticsearch-local)
* [Chrome browser](https://www.google.com/chrome/)

Now, let's look how to get things up and running to use the tests.

### **Magento installation**

1. First, install [MAGENTO 2](https://magento.com/) using Docker via this link:

    https://github.com/markshust/docker-magento#setup

2. Choose Automated Setup with sample data.

3. Note that you will be prompted for your system password during setup.

4. You should have port 80, 443, 3306 and 9000 available in order to run magento. Here is a [video instruction](https://courses.m.academy/courses/setup-magento-2-development-environment-docker/lectures/8974570) for setup.

5. During the setup you will be asked to enter you authentification keys. Learn how to create them [here](https://devdocs.magento.com/guides/v2.3/install-gde/prereq/connect-auth.html).

6. You will be given your Magento Admin URI. Please save it for the next step. It starts with: `https://magento2.test/admin_`

7. After the setup completes running, you should be able to access your site at https://magento2.test.

### **Configuring Catalog Search**

1. Go to your Magento Admin URI and enter the credentials below:
    Username: `john.smith`
    Password: `password123`

2. The default search engine used by Magento is MySQL. To change it to Elasticsearch follow the [guide](https://docs.magento.com/user-guide/catalog/search-elasticsearch.html#step-1-configure-search-options). 

3. Choose the following configurations:
    * Enable Search Suggestions: _Yes_.
    * Search Suggestions Count: _2_.
    * Show Results Count for Each Suggestion: _No_.

Magento is configured! Let's move on to the next part.

4. For reference, you can have a look at a [demo website](http://demo.magento-elastic-suite.io/index.php), similar to the one tested. This demo website has custom configuration, so tests do not take this into account and shall not be run against it.

### **Setup of testing environment**   

In this step the following is installed:
* virualenv
* [SeleniumBase](https://seleniumbase.io/)
* pytest
* chromedriver

1. Clone this repository and go to folder

```bash
git clone https://github.com/kate-tel/magento2.test.git
cd magento2.test
```

2. Install virtualenv

```bash
pip3 install -U pip
pip3 install virtualenv
```

3. Create & activate virtual env

```bash
virtualenv .venv
source .venv/bin/activate
```

4. Install requirements. As a result, seleniumbase and pytest will be installed.

```bash
pip3 install -r requirements.txt
```

5. Install chromedriver

```bash
seleniumbase install chromedriver latest
```

Now project environment is configured and tests can be run.

### **Running the tests**

1. Specify a test suite to run:
```bash
pytest magento/tests/mag_test_search.py
```

2. To select a specific test method to run, indicate class name and then method name:

```bash
pytest magento/tests/mag_test.py::MagentoTestClass::test_search_fail
```

3. Alternatively, you can specify a test to run, using pytest markers. Each test has its own marker for this purpose.

Running a specific test:

```bash
pytest magento/tests/mag_test.py -m=minicart
```

4. Sometimes page load duration is unstable, so in case of **ElementNotVisibleException**, running the test(-s) with a custom settings file will help. In this file timeouts are extended, compared to the default ones.

Running a test with custom settings:

```bash
pytest magento/tests/mag_test.py -m=search --settings_file=custom_settings.py
```

### **Project content**

The project consists of two main parts: test suites and page objects files.
```
.
├── __init__.py
├── custom_settings.py 
├── magento 
│   ├── page_objects
│   │   ├── mag_object_cart.py 
│   │   ├── mag_object_catalog.py 
│   │   ├── mag_object_checkout.py
│   │   └── mag_object_main.py 
│   └── tests
│       ├── __init__.py
│       ├── mag_test.py
│       └── mag_test_search.py
├── pytest.ini
├── README.md
└── requirements.txt

```

### **References**

1. For SeleniumBase CLI commands, log saving, configurations etc, please have a look at https://github.com/seleniumbase/SeleniumBase.

2. List of SeleniumBase methods:

https://github.com/seleniumbase/SeleniumBase/blob/master/seleniumbase/fixtures/base_case.py
