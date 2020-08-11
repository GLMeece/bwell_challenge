​@desktop @web

​Feature:​ BWell Automation QA Task
  As a QA who is interested in BWell
  I want to solve interview task
  So that I can be confident if get invited on a meeting
​
Scenario:​ ​User can Sign in with valid credentials
    ​Given ​I am on ​"http://login.myappcms.com/"​ home page
    When​ I type ​"CMS Demo Account"​ as App Name
    And​ I type ​"demo@diyappdesigner.com"​ as Email address
    And​ I type ​"demo123"​ as Password
    And​ I click on Sign in button
    Then​ I should see my Dashboard

# ​Scenario:​ ​User can sort in ascending order all Appointments services by name
#     Given​ I am on ​"http://login.myappcms.com/build"​ page
#     When​ I click ​"Sort Ascending"​ on ​"Service Name"​ column
#     Then​ I should see correct results list

# ​Scenario:​ User can search all Appointments services by name
#     ​Given​ I am on ​"http://login.myappcms.com/build"​ page
#     When​ I type ​"colour"​ in the Search box
#     Then​ I should see correct results list

