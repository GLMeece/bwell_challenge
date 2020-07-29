# Assignment: Test Functionality of a Given Web Page - Manually

## Background

This exercise is intended to demonstrate the mindset of the candidate in developing _manual_ test cases, leveraging a Feature description as a starting point.

| Candidate  | E-Mail            | LinkedIn | GitHub Link|
| ---------- | ----------------- | ---------- | ---------- |
| Greg Meece | glmeece@gmail.com | https://www.linkedin.com/in/gregmeece/ | https://github.com/GLMeece/bwell_challenge |

## Presuppositions

* The Gherkin syntax is _behavioral_ not _procedural_. IOW, it focuses on what the user would like to accomplish vs. the specific granular steps needed to accomplish a given task.
* Gherkin's **Given**, **When**, **Then** syntax favors high-level, abstracted implementation.
* Scenario's [should be stated in the 3rd person](https://automationpanda.com/2017/01/18/should-gherkin-steps-use-first-person-or-third-person/) to avoid confusion of persona roles.
* Although Scenarios are considered stand-alone, within a given Feature file, Scenarios are executed sequentially. This allows us to reduce the level of Scenario overhead to test sections of functionality which

## Origin Feature

The following Feature description is our starting point for subsequent manual testing scenarios.

```gherkin
Feature: BWell Testing task
  As a User who is interested in CMS platforms
  I want to create Appointments
  So that I can plan my activities at "http://login.myappcms.com/build"
```

## Test Scenarios

The following test scenarios are also located in tablular form in the CSV file named X in the same directory as this README. They are shown inline as an easier-to-read format alternative.

```gherkin
Feature: BWell Testing task
  As a User who is interested in CMS platforms
  I want to create Appointments
  So that I can plan my activities at "http://login.myappcms.com/build"
    
  Background:
    Given the user is on the "http://login.myappcms.com/" home page
    And they type "CMS Demo Account" as the App Name
    And they type "demo@diyappdesigner.com" as the Email address
    And they type "demo123" as the Password
    When they click on Sign in button
    Then they should see the CMS Demo Account Dashboard
    
  Scenario: User can see Add Service Appointment form
    Given the user is on the CMS Demo Account Dashboard page
    When the user clicks on the Appointments item in the sidebar
    And the user clicks on the Services sub-item below the Appointments item
    And the user clicks on the Add button under the Services tab
    Then the user can see the Services addition form
    
  Scenario Outline: User Adds Service Appointment
    Given the user has clicked the Add button
    When the user enters the value "<value>" in the field "<fieldname>"
    And the user clicks on the Save button
    Then the Service Name should be evident in the Services list
    
    Examples: Fields
      | fieldname | value |
      | Service Name | With a Smile |
      | Service Description | It's our middle name |
      | Duration | 1:10 |
      | Price | 20.00 |
      | Opening Hours | 08:00 - 17:00 |
      | Image | https://www.freepnglogos.com/uploads/cucumber-png/cucumber-slice-hydrate-photo-pixabay-23.png |
      | Column7 | Collum 7 |
      | Column8 | Call 'em 8 |
      | Sheet1 | Sheets to the wind |
    
  Scenario: User can Update Services Appointment entry
    Given the user is on the Services list pane
    When the user clicks the Edit (pencil) icon for the previously-created appointment
    And the user changes the Service Name to "Testing Services"
    And the user clicks on the Save button
    Then the updated Service Name "Testing Services" should be evident in the Services list
    
  Scenario: User can Delete Services Appointment entry
    Given the user is on the Services list pane
    When the user clicks the Delete (trashcan) icon for the previously-created appointment "Testing Services"
    And the user clicks Yes in response to "Are you sure you want to remove this item?"
    Then the previously-created Service Name "Testing Services" should be removed from the Services list
```


