# Flip-Automation-Behave-Selenium

BDD framework built using Python and Behave to support automation testing of websites on various browsers. This project tries to automate simple open link menu flow on [Flip.id](flip.id) site.

## Built with

* python 3.9.10
* behave 1.2.6
* selenium 4.1.0
* Pycharm Community >= 2021.3.2
* allure-behave 2.9.45
* allure-commandline 2.17.2

## Pre-requisites and Installations

### Cloning the repository
You can get a copy of all files used in this tutorial by cloning this repository!

```shell
git clone https://github.com/manami27/Flip-Engineer-Test.git
```
```shell
cd Flip-Engineer-Test
```

### Installations
To automate the test, you need to install required component:

1. Python 2.7.14 or above. You can download it from [here](https://www.python.org/downloads/release/python-360/). 

2. To install python package manager (pip). It can be downloaded from its [download page](https://pip.pypa.io/en/stable/installation/). All further installations in the blog post will make use of pip so it’s highly recommended to install it.

3. A development environment. The PyCharm Community edition will be used in this blog post. You can download it from the [Pycharm website](https://www.jetbrains.com/pycharm/). You can use any IDE of your choice since code snippets are not IDE dependent.

4. Installing Python bindings for Selenium. Use [pip](https://pip.pypa.io/en/latest/installation/) to install the selenium package. Python 3 has pip available in the [standard library](https://docs.python.org/3/installing/index.html). Using pip, you can install selenium like this:
```
    pip install selenium
```

5. Behave-webdriver is a step library intended to allow users to easily write [Selenium](http://seleniumhq.org/) webdriver tests with the behave BDD testing framework. For more details, see the [behave-webdriver documentation](https://behave-webdriver.readthedocs.io/en/stable/). Using pip, you can install behave-webdriver like this:
```
    pip install behave-webdriver
```

6. Using webdrivers. Selenium requires that you provide executables for the webdriver you want to use. Place your downloaded driver inside the folder C:\\<phyton_instalation_folder>\Scripts, and make sure it’s in your PATH. See these [driver installation notes](https://selenium-python.readthedocs.io/installation.html#drivers) for more details.

7. Allure report. Allure is based on standard xUnit results output but adds some supplementary data. Any report is generated in two steps. See [examples](https://github.com/allure-examples) and [documentation](https://github.com/allure-framework/allure1/wiki) for more details. Installation is easy via pip. And make sure to add allure to your system PATH.
```
    pip install allure-behave
```
8. Allure Commandline is a tool to generate Allure report from test results. You can download it from [here](https://docs.qameta.io/allure/).

Running the tests
----------------
* To run the test with allure report
```behave -f allure_behave.formatter:AllureFormatter -o reports/ features/flipmenu.feature```

* To run the test without allure report
```behave features/flipmenu.feature```

* To generate the html allure report from the json files inside reports folder**
```allure serve reports/```


Scenario on the feature file
------------------------

```gherkin

    # Flip-Engineer-test/features/flipmenu.feature

    Feature: Open flip menu feature
    Background: common steps
        Given launch chrome browser
        When open flip landing page
        When verify success open landing page

    Scenario: Open login page
        When navigate to masuk menu
        Then verify success open login page

    Scenario: Open produk page
        When navigate to produk menu
        Then verify success open layanan flip page

    Scenario: Open karir page
        When navigate to karir menu
        Then verify success open karir page
 ```
