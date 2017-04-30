
Feature: Login Page

  Scenario: Login
    When a user visits the login page
    Then she should see the username field
    And she should see the email field
    And she should see the password field
    And she should see the login button

  Scenario: Login Success
    When a user visits the login page
    And she logs in with username "yvonne" and email "yvonne@gmail.com" and password "Yvonne1215"
    Then she should see a message of login success

  Scenario: Login Failure
    When a user visits the login page
    And she logs in with username "baduser" and email "yvonne@gmail.com" and password "badpasswd"
    Then she should see a message of login failure

#   Scenario: Logout
#     Given a user visits the login page
#     And she sees the Logout link
#     When she clicks on the Logout link
#     Then she returns to the site
#     And she sees a message telling her she has logged out

