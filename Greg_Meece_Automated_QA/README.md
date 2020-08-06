# Assignment: Test Functionality of a Given Web Page - Automated

## Background

This exercise is intended to demonstrate the mindset of [the candidate](https://www.icanbwell.com/careers#sr-qa-engineer) in developing _manual_ test cases, leveraging a Feature description as a starting point.

| Candidate  | E-Mail            | LinkedIn                               | GitHub Link                                |
| ---------- | ----------------- | -------------------------------------- | ------------------------------------------ |
| Greg Meece | glmeece@gmail.com | https://www.linkedin.com/in/gregmeece/ | https://github.com/GLMeece/bwell_challenge |

# Automation Setup & Execution

The author has decided to avoid OS and machine-specific compatability issues and utilize container technology - specifically [Docker](https://www.docker.com/resources/what-container).
![Jules prefers Docker](https://memegenerator.net/img/instances/81997572/say-works-on-my-machine-one-more-time.jpg)

1. If not done already, [install Docker](https://www.docker.com/get-started) on the SUT. You will most likely have to restart your machine after installation. Additional installation may be required for Windows (installing or updating the WSL); follow the prompts and you should be OK.

2. It is _highly_ recommended you install (or verify the install of) **Make** on the SUT. Both macOS and Linux should already have Make installed, so for Windows:

   1. Go to the [Make for Windows](http://gnuwin32.sourceforge.net/packages/make.htm) page and click on the _Complete package, except sources_ [Setup](http://gnuwin32.sourceforge.net/downlinks/make.php) link.
   2. Run the downloaded installer file.
   3. You will need to [add the path](https://www.computerhope.com/issues/ch000549.htm#windows10) for `make.exe`; `C:\Program Files (x86)\GnuWin32\bin`. After saving changes, when you open a command prompt, you should be able to invoke `make` commands.

3. If you have `make` installed, xxx

4. In a terminal, change into the repo directory and execute: `docker build -t glmeece/bwell_challenge .`

5. Next, execute: `docker run --name bwell_container -it glmeece/bwell_challenge:latest /bin/bash`
   **Note**: If you have executed this step before, you should execute the following command _before_ executing this command again:

   ```bash
   docker kill bwell_container || true
   docker rm bwell_container || true
   ```

6. EXECUTION HERE

7. Once finished, execute `exit` to stop container.

     


## Presuppositions

* The Gherkin syntax is _behavioral_ not _procedural_. IOW, it focuses on what the user would like to accomplish vs. the specific granular steps needed to accomplish a given task.
* Gherkin's **Given**, **When**, **Then** syntax favors high-level, abstracted implementation.
* Scenario's [should be stated in the 3rd person](https://automationpanda.com/2017/01/18/should-gherkin-steps-use-first-person-or-third-person/) to avoid confusion of persona roles.
* Although Scenarios are considered stand-alone, within a given Feature file, Scenarios are executed sequentially. This allows us to reduce the level of Scenario overhead to test sections of functionality which in turn reduces redundancy.





https://www.icanbwell.com/careers#sr-qa-engineer



https://cucumber.io/docs/gherkin/reference/



https://automationpanda.com/2018/10/22/python-testing-101-pytest-bdd/

https://github.com/pytest-dev/pytest-bdd



seleniumbase install chromedriver

### Login Information

Log into the CMS using the following credentials.

- **CMS Login:** [http://cms.diyappdesigner.com](http://cms.diyappdesigner.com/)
- **App Name:** `CMS Demo Account`

- **Email address:** `demo@diyappdesigner.com`

- **Password:** `demo123`

## Origin Feature

The following Feature description is our starting point for subsequent manual testing scenarios.

```gherkin
Feature: BWell Automation QA Task
  As a QA who is interested in BWell
  I want to solve interview task
  So that I can be confident if get invited on a meeting
```


## Test Scenarios

The following test scenarios are also located in tablular form in the CSV file named X in the same directory as this README. They are shown inline as an easier-to-read format alternative.

```gherkin
@desktop @web
#As a <type of user> I want <some goal> so that <some reason>

Feature: BWell Automation QA Task
  As a QA who is interested in BWell
  I want to solve interview task
  So that I can be confident if get invited on a meeting

Scenario: User can Sign in with valid credentials
  Given I am on "http://login.myappcms.com/" home page
  When I type "CMS Demo Account" as App Name
  And I type "demo@diyappdesigner.com" as Email address
  And I type "demo123" as Password
  And I click on Sign in button
  Then I should see my Dashboard

Scenario: User can sort in ascending order all Appointments services by name
  Given I am on "http://login.myappcms.com/build" page
  When I click "Sort Ascending" on "Service Name" column
  Then I should see correct results list

Scenario: User can search all Appointments services by name
  Given I am on "http://login.myappcms.com/build" page
  When I type "colour" in the Search box
  Then I should see correct results list
```