#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Simple 'does it work' test verifying that Selenium, Chrome, and Chromedriver
# are all installed and that we can connect to the network
# - Greg Meece

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

print("\n ✓ Imports completed")
chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--headless")
print(" ✓ Chrome options initialized")
driver = webdriver.Chrome(options=chrome_options)
print(" ✓ Selenium Driver initialized")
start_url = "http://www.python.org"
driver.get(start_url)
print(" ✓ Visited Python.org")
assert "Welcome to Python.org" in driver.title
print(" ✓ Python's web page has the correct title")
driver.quit()
print("\n ✔︎ You can leverage Selenium testing from this container\n")
