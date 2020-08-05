# Assignment: Test Functionality of a Given Web Page - Manually

## Background

This exercise is intended to demonstrate the mindset of the candidate in developing _manual_ test cases, leveraging a Feature description as a starting point.

| Candidate  | E-Mail            | LinkedIn | GitHub Link|
| ---------- | ----------------- | ---------- | ---------- |
| Greg Meece | glmeece@gmail.com | https://www.linkedin.com/in/gregmeece/ | https://github.com/GLMeece/bwell_challenge |

## Execution

The test cases indicated in this README will be executed manually. The test scenarios are written using the Gherkin/BDD-style that should be understandable by any experienced QA personnel.

## Presuppositions

* The Gherkin syntax is _behavioral_ not _procedural_. [IOW](https://www.allacronyms.com/IOW/In_Other_Words), it focuses on _what the user would like to accomplish_ vs. the _specific granular steps_ needed to accomplish a given task.
* Gherkin's **Given**, **When**, **Then** syntax favors high-level, abstracted implementation.
* Scenario's [should be stated in the 3rd person](https://automationpanda.com/2017/01/18/should-gherkin-steps-use-first-person-or-third-person/) to avoid confusion of persona roles.
* Although Scenarios are considered stand-alone, within a given Feature file, Scenarios are executed sequentially. This allows us to reduce the level of Scenario overhead to test sections of functionality which in turn reduces redundancy.

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
  Given the user is on the Services addition form
  And the user has clicked the Add button
  When the user enters the value "<value>" in the field "<fieldname>"
  And the user clicks on the Save button
  Then the Service Name, Service Description, Duration, Price and Opening Hours should be evident in the Services list
  
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
    
Scenario: User can Cancel an Update Services Appointment entry
  Given the user is on the Services list pane
  When the user clicks the Edit (pencil) icon for the previously-created appointment
  And the user changes the Service Name from "Testing Services" to "Service Not Saved"
  And the user clicks on the Cancel button
  Then the Service Name "Testing Services" should still be evident in the Services list
    
Scenario: User can Delete Services Appointment entry
  Given the user is on the Services list pane
  When the user clicks the Delete (trashcan) icon for the previously-created appointment "Testing Services"
  And the user clicks Yes in response to "Are you sure you want to remove this item?"
  Then the previously-created Service Name "Testing Services" should be removed from the Services list
  
# - - - - - - - - - - - - - - - - - - - - - - - - -
# Additional Feature

Feature: CMS Blog Functionality Tests
  As a QA Tester evaluating the CMS Demo Account
  I want to examine the Blog posts section
  So that I can be assured creation and editing works properly
    
Background:
    Given the user is on the "http://login.myappcms.com/" home page
    And they type "CMS Demo Account" as the App Name
    And they type "demo@diyappdesigner.com" as the Email address
    And they type "demo123" as the Password
    When they click on Sign in button
    Then they should see the CMS Demo Account Dashboard
    
Scenario: User can view Blog creation form
  Given the user is on the CMS Demo Account Dashboard page
  When the user clicks on the Blog item in the sidebar
  And the user clicks on the Add button in the Blog pane
  Then the user can see the Blog addition form
  
Scenario Outline: User Adds New Blog post
  Given the user is on the Blog creation form
  When the user enters the value "<value>" in the field "<fieldname>"
  And the user clicks on the Save button
  Then the Blog Title, Image, Author, and Date should be evident in the Blog list
    
  Examples: Fields
    | fieldname | value |
    | Title | Gherkin without the Pickle |
    | Image | http://messageconsulting.com/wp-content/uploads/2016/04/CucumberLogo.png |
    | Author | Otto Mayter |
    | Date | 01-08-2020 15:00 |
    | Category | [lang_EN]Technology[/lang_EN][lang_PT]Tecnologia[/lang_PT] |
    | Intro | Learning Gherkin is not as hard as you might think! |
    | Content | Read this article for a good start. |
    | URL | https://cucumber.io/docs/gherkin/reference/ |
    | Tags | programming, cucumber, bdd |

Scenario: User can Update Blog entry
  Given the user is on the Blog list pane
  When the user clicks the Edit (pencil) icon for the previously-created blog entry
  And the user changes the Blog Title to "Cucumber - Not Just Ruby Any More!"
  And the user clicks on the Save button
  Then the updated Blog Title "Cucumber - Not Just Ruby Any More!" should be evident in the Blog list
    
Scenario: User can Cancel an Blog Update
  Given the user is on the Blog list pane
  When the user clicks the Edit (pencil) icon for the previously-created blog entry
  And the user clicks the Draft checkbox
  And the user clicks on the Cancel button
  Then the value of False should be evident in the Blog list for that blog entry
    
```


