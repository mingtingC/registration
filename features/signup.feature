Feature: Register Page

  Scenario: Register
    When a user visits the register page
    Then she should see the name field
    And she should see the password field
    And she should see the confirm password field
    And she should see the register button


  Scenario: Register Failure1
    When a user visits the register page
    And she signs up with username "gogogostn" and email "stn131415@gamil.com" and password "12345678" and confirm_password "12345677"
    Then she should see a message of Password and confirm password are not the same

  Scenario: Register Failure2
    When a user visits the register page
    And she signs up with username "gogogostn" and email "stn131415@gamil.com" and password "12345678" and confirm_password "12345678"
    Then she should see a message of Not a Valid Password

  Scenario: Register Failure3
    When a user visits the register page
    And she signs up with username "gogogostn" and email "stn131415@gamil.com" and password "1234567a" and confirm_password "1234567a"
    Then she should see a message of Not a Valid Password

  Scenario: Register Failure4
    When a user visits the register page
    And she signs up with username "gogogostn" and email "stn131415@gamil.com" and password "12345aA" and confirm_password "12345aA"
    Then she should see a message of Not a Valid Password

 Scenario: Register Success
    When a user visits the register page
    And she signs up with username "gogogostn" and email "stn131415@gamil.com" and password "1234567aA" and confirm_password "1234567aA"
    Then she turns to show_entries
#
#  Scenario: Register Failure5
#    When a user visits the register page
#    And she signs up with username "admin" and email "stn131415@gamil.com" and password "123456Aa" and confirm_password "123456Aa"
#    Then she should see a message of User name has already existed, please try again


  Scenario: Register Link test
    Given a user visits the site
     Then she should see the Register link
     When she clicks on the Register link
     Then she turns to register page
