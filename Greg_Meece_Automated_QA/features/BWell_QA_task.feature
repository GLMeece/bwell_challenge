@desktop @web
Feature: BWell Automation QA Task
  As a QA engineer who is interested in BWell
  I want to solve the interview automation task
  So that I can be confident I understand BDD if get invited to a follow-up interview


  Scenario: User can Sign in with valid credentials
    Given the user is on the "http://login.myappcms.com/" home page
    When the user enters the correct login information
    Then the user should see the Dashboard


  Scenario: User can sort in ascending order all Appointments services by name
    Given the user is on the CMS Demo Account page
    When the user clicks "Sort Ascending" on "Service Name" column
    Then the user should see results sorted alphabetically by Service Name


  Scenario: User can search all Appointments services by name
    Given the user is on the CMS Demo Account page
    When I type "colour" in the Search box
    Then I should see correct results list
