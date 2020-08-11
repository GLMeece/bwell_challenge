"""
Page object classes to encapsulate selectors and logic for helper methods
"""

import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HelperFunctions():

    @classmethod
    def enter_default_login_info(cls, browser):
        logging.debug("Enter default login values, log in")
        browser.get(LoginPage().login_url)
        assert browser.current_url == LoginPage().login_url
        browser.find_element_by_id(LoginPage().application_name_id).send_keys(
            LoginPage().application_txt)
        browser.find_element_by_id(LoginPage().username_field_id).send_keys(
            LoginPage().username_txt)
        browser.find_element_by_id(LoginPage().password_field_id).send_keys(
            LoginPage().password_txt)
        browser.find_element_by_id(LoginPage().signin_button_id).click()

    @classmethod
    def login(cls, browser):
        logging.debug("Logging in via Login function")
        cls.enter_default_login_info(browser)
        WebDriverWait(browser, timeout=7).until(
            EC.title_is(DashboardPage().cms_title))

    @classmethod
    def display_services_table(cls, browser):
        """Navigates to show Services table"""
        logging.debug("Displaying Services Table")
        browser.find_element_by_id(DashboardPage().appointments_id).click()
        WebDriverWait(browser, 10).until(EC.visibility_of_element_located((
            By.ID, DashboardPage().services_menu_item_id)))
        browser.find_element_by_id(
            DashboardPage().services_menu_item_id).click()
        # When 'Loading...' class isn't visible, the table should be loaded...
        WebDriverWait(browser, 10).until(EC.invisibility_of_element_located((
            By.CSS_SELECTOR, '.x-mask-msg-text')))

    @classmethod
    def service_name_as_list(cls, browser):
        """Returns all populated Service Names from the Services table"""
        logging.debug("Gathers all Service Names in Service table")
        # When 'Loading...' class isn't visible, the table should be loaded...
        WebDriverWait(browser, 10).until(EC.invisibility_of_element_located((
            By.CSS_SELECTOR, '.x-mask-msg-text')))
        service_name_list = []
        rows = browser.find_elements_by_xpath(
            DashboardPage().service_table_rows_xpath)
        logging.debug(f"Row count: {len(rows)}\n")
        for row in rows:
            first_col = row.find_element_by_xpath('./td[1]')
            if len(first_col.text) > 0:
                logging.debug(f"'{first_col.text}'")
                service_name_list.append(first_col.text)
        return service_name_list


# ----------------------------------------------------------------


class LoginPage():
    """Selectors and values for Login page"""
    login_url = "http://login.myappcms.com/"
    language_dropdown_id = "select2-drop-mask"
    application_name_id = "appName"
    username_field_id = "username"
    password_field_id = "password"
    signin_button_id = "login-submit"
    application_txt = "CMS Demo Account"
    username_txt = "demo@diyappdesigner.com"
    password_txt = "demo123"

# ----------------------------------------------------------------


class DashboardPage():
    """Selectors and values for Dashboard page"""
    dashboard_url = "http://login.myappcms.com/build"
    cms_title = "My App CMS"
    appointments_id = "appitemId-00d010a0-d019-11e8-8605-0003ffbb5e34"
    services_menu_item_id = "appitemId-00d010a1-d019-11e8-8605-0003ffbb5e34"
    service_name_xpath = "//div/span[text()='Service Name']"
    sort_service_name_xpath = \
        "//div/span[text()='Service Name']//following-sibling::div"
    sort_service_asc_xpath = \
        "//a/span[text()='Sort Ascending']//following-sibling::div"
    sort_service_desc_xpath = \
        "//a/span[text()='Sort Descending']//following-sibling::div"
    services_table_body_id = "gridview-1044-body"
    service_name_cell_css = "#gridview-1044-body > tr > td:first-child"
    service_table_rows_xpath = "//table/tbody/tr"
    service_table_search_button_css = "tbody tr td input[placeholder='Search']"
