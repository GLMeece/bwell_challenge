# Assignment: Test Functionality of a Given Web Page - Automated

## Background

This exercise is intended to demonstrate the mindset of [the candidate](https://www.icanbwell.com/careers#sr-qa-engineer) in developing _automated_ test cases, leveraging a Feature description as a starting point.

| Candidate  | E-Mail            | LinkedIn                               | GitHub Link                                |
| ---------- | ----------------- | -------------------------------------- | ------------------------------------------ |
| Greg Meece | glmeece@gmail.com | https://www.linkedin.com/in/gregmeece/ | https://github.com/GLMeece/bwell_challenge |

# Automation Setup & Execution

The author has decided to avoid OS and machine-specific compatability issues and utilize container technology - specifically [Docker](https://www.docker.com/resources/what-container). This will largely eliminate the need for much setup effort.

If the user to set up a Python virtual environment and install the package requirements (i.e., `pip install -r requirements.txt`) should you choose to do so. Additionally, you will need to install [Chromedriver](https://sites.google.com/a/chromium.org/chromedriver/) on the SUT in order to execute the tests. If you desire to see the Chrome browser actually run in this environment (which is not possible within Docker), edit the `Greg_Meece_Automated_QA/step_defs/test_BWell_QA_task.py` file such that the line `chrome_options.add_argument("--headless")` is commented out.

## Setup

1. If not done already, [install Docker](https://www.docker.com/get-started) on the SUT. You will most likely have to restart your machine after installation. Additional installation may be required for Windows (e.g., installing or updating the WSL); follow the prompts and you should be OK.
2. If running under windows, place the repository in a path _without_ spaces. We are mounting the repository directory as a volume within Docker, and the `%cd%` variable does not properly escape spaces, which Docker does not like. For example:
   * **Yes**: `C:\my\path\without\spaces\bwell_challenge`
   * **No**:  `C:\Users\My Name\Documents\My Repos\GitHub\bwell_challenge`

## Execution

Instructions included both _with_ and _without_ `make` installed. Both assume you have a terminal running and you've changed into the root of the repository.

### With Make (macOS or Linux)

1. Build the container first (may take awhile the first time): `make build`
2. Run the container: `make dev`
3. Run the tests: `make run` (or, alternately just run `pytest`)
4. When finished with the tests, execute `exit` to stop the container instance.

### Without Make (Windows)

1. Execute: `docker build -t glmeece/bwell_challenge .`

2. Run the container: `docker run -v %cd%:/opt/bwell --name bwell_challenge -it glmeece/bwell_challenge /bin/bash`
   **Note**: If you have executed this step before, you should execute the following command _before_ executing this command again:

   ```bash
   docker rm bwell_challenge
   ```

4. Run the tests: `pytest`

5. Once finished, execute `exit` to stop the container.

With both approaches, you will find an HTML report (`bwell_report.html`) in the repo path:
`Greg_Meece_Automated_QA/reports/`


## Presuppositions

* The Gherkin syntax is _behavioral_ not _procedural_. IOW, it focuses on what the user would like to accomplish vs. the specific granular steps needed to accomplish a given task.
* Gherkin's **Given**, **When**, **Then** syntax favors high-level, abstracted implementation.
* Scenario's [should be stated in the 3rd person](https://automationpanda.com/2017/01/18/should-gherkin-steps-use-first-person-or-third-person/) to avoid confusion of persona roles.
* Although Scenarios are considered stand-alone, within a given Feature file, Scenarios are executed sequentially. This allows us to reduce the level of Scenario overhead to test sections of functionality which in turn reduces redundancy.

### Login Information

For reference, logging into the CMS will use the following information since the author determined it was more useful to abstract this:

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

The following test scenarios were given as testing scenarios for automation:

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

However, these scenarios seem to be written with a _procedural_ rather than a _behavioral_ mindset. As such, the author has rewritten them as follows:

```gherkin
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
  When the user types "colour" in the Search box
  Then the user should see correct results list
```

## Closing Thoughts

