# coding=utf-8
"""
This module contains step definitions for BWell_QA_task.feature.

features/BWell_QA_task.feature feature tests.
"""

import logging

import pytest
from pytest_bdd import (
    given,
    scenario,
    then,
    when,
    parsers
)
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .page_objects import (LoginPage as LogPg, DashboardPage as DashPg,
                           HelperFunctions as Help)


# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ LOGGING SETUP ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ 


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(filename)-22s| %(levelname)-s -> %(message)s",
    datefmt="%m/%d/%Y %I:%M:%S %p"
)
LOG = logging.getLogger()


# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ PYTEST FIXTURES ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ 


@pytest.fixture
def browser():
    wait_for_it = 25
    chrome_options = Options()
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--headless")  # Enable for Docker run
    crmbrowse = webdriver.Chrome(options=chrome_options)
    crmbrowse.implicitly_wait(wait_for_it)
    crmbrowse.set_page_load_timeout(wait_for_it)
    yield crmbrowse
    crmbrowse.quit()


# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ SCENARIOS ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ 


@scenario('../features/BWell_QA_task.feature',
          'User can Sign in with valid credentials')
def test_user_can_sign_in_with_valid_credentials():
    """User can Sign in with valid credentials."""
    LOG.info("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
    LOG.info(" ✓ SCENARIO: User can Sign in with valid credentials.")
    LOG.info("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")


@scenario('../features/BWell_QA_task.feature',
          'User can sort in ascending order all Appointments services by name')
def test_user_can_sort_in_ascending_order_appointments_services_by_name():
    """User can sort in ascending order all Appointments services by name."""
    LOG.info("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
    LOG.info(" ✓ SCENARIO: User can sort in ascending order all Appointments "
             "services by name.")
    LOG.info("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")


@scenario('../features/BWell_QA_task.feature',
          'User can search all Appointments services by name')
def test_user_can_search_all_appointments_services_by_name():
    """User can search all Appointments services by name."""
    LOG.info("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
    LOG.info(" ✓ SCENARIO: User can search all Appointments services by name.")
    LOG.info("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")


# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ GIVEN Steps ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ 


@given(parsers.parse('the user is on the "{URL}" home page'))
def i_am_on_the_web_page(browser, URL):
    """Scenarios:
    User can Sign in with valid credentials
    User can sort in ascending order all Appointments services by name
    User can search all Appointments services by name
    """
    LOG.debug(f"Sending browser to '{URL}'")
    browser.get(URL)
    assert browser.current_url == URL
    LOG.info(f"GIVEN STEP: the user is on the '{URL}' home page")


@given('the user is on the CMS Demo Account page')
def logged_in_and_on_cms_page(browser):
    LOG.debug("Verifying user is logged in")
    Help.login(browser)
    WebDriverWait(browser, timeout=25).until(
        EC.title_is(DashPg.cms_title))
    assert browser.title == DashPg.cms_title
    LOG.info("GIVEN STEP: the user is on the CMS Demo Account page")


# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ WHEN Steps ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ 


@when('the user enters the correct login information')
def enter_correct_login_info(browser):
    """Scenario:
    User can Sign in with valid credentials
    """
    Help.enter_default_login_info(browser)
    LOG.info("WHEN STEP: the user enters the correct login information")


@when(parsers.parse('I type "{app_name_input}" as App Name'))
def type_app_name(browser, app_name_input):
    """Scenario:
    User can Sign in with valid credentials
    """
    LOG.debug(f"app_name_input: {app_name_input}")
    browser.find_element_by_id(LogPg.application_name_id).send_keys(
        f"{app_name_input}")


@when(parsers.parse('I type "{email_input}" as Email address'))
def type_email_address(browser, email_input):
    """Scenario:
    User can Sign in with valid credentials
    """
    LOG.debug(f"email_input: {email_input}")
    browser.find_element_by_id(
        LogPg.username_field_id).send_keys(f"{email_input}")


@when(parsers.parse('I type "{password_input}" as Password'))
def type_password(browser, password_input):
    """Scenario:
    User can Sign in with valid credentials
    """
    LOG.debug(f"password_input: {password_input}")
    browser.find_element_by_id(
        LogPg.password_field_id).send_keys(f"{password_input}")


@when('I click on Sign in button')
def click_sign_in_button(browser):
    """Scenario:
    User can Sign in with valid credentials
    """
    browser.find_element_by_id(LogPg.signin_button_id).click()
    get_title = browser.title
    LOG.debug(f"Current title: '{get_title}'")


@when(parsers.parse('the user clicks "Sort Ascending" on "Service Name" column'))
def sort_on_column(browser):
    """I click "Sort Ascending" on "Service Name" column."""
    Help.display_services_table(browser)
    browser.find_element_by_xpath(DashPg.service_name_xpath).click()
    LOG.info(
        'WHEN STEP: the user clicks "Sort Ascending" on "Service Name" column')


@when(parsers.parse('I type "{search_string}" in the Search box'))
def i_type_string_in_the_search_box(browser, search_string):
    """I type "colour" in the Search box."""
    Help.display_services_table(browser)
    browser.find_element_by_css_selector(
        DashPg.service_table_search_button_css).send_keys(search_string)
    LOG.info('WHEN STEP: I type "colour" in the Search box')


# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ THEN Steps ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ 


@then('the user should see the Dashboard')
def dashboard_title_is(browser):
    WebDriverWait(browser, timeout=25).until(
        EC.title_is(DashPg.cms_title))
    assert browser.title == DashPg.cms_title
    LOG.info("THEN STEP: the user should see the Dashboard")


@then('the user should see results sorted alphabetically by Service Name')
def results_are_sorted_alphabetically(browser):
    """I should see correct results list."""
    service_names = Help.service_name_as_list(browser)
    LOG.debug(f"'As-is' Service Names:\n{service_names}")
    service_names_forced_sort = sorted(service_names, key=str.lower)
    LOG.debug(
        f"Service Names programmatically sorted:\n{service_names_forced_sort}")
    assert service_names_forced_sort == service_names
    LOG.info("THEN STEP: the user should see results sorted alphabetically "
             "by Service Name")


@then('I should see correct results list')
def i_should_see_correct_results_list(browser):
    """I should see correct results list."""
    service_names = Help.service_name_as_list(browser)
    LOG.debug(f"Service Names list:\n{service_names}")
    assert 'colour' in service_names
    LOG.info("THEN STEP: I should see correct results list")
