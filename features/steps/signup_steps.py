from behave import given, when, then, use_step_matcher, Given, When
from hamcrest import assert_that, equal_to
import re
from login_utils import *
import time



@when(u'a user visits the register page')
def visit_register(context):
    context.browser.get(context.server_address + "/signup")
    time.sleep(1)


@then(u'she should see the confirm password field')
def see_passwordConfirm_field(context):
    flaskr_found = re.search("Confirm the password.", context.browser.page_source, re.IGNORECASE)
    assert flaskr_found


@then(u'she should see the register button')
def see_register_button(context):
    flaskr_found = re.search("sign up", context.browser.page_source, re.IGNORECASE)
    assert flaskr_found


@when(u'she signs up with username "{username}" and email "{email}" and password "{password}" and confirm_password "{confirm_password}"')
def register(context, username, email, password, confirm_password):
    print(1)
    context.browser.get(context.server_address + "/signup")
    uname = context.browser.find_element_by_name('name')
    email1 = context.browser.find_element_by_name('email')
    passwd = context.browser.find_element_by_name('password')
    passwd1 = context.browser.find_element_by_name('confirm_password')
    login_button = context.browser.find_element_by_name('signup')
    print(2)
    uname.clear();
    email1.clear();
    passwd.clear();
    passwd1.clear();
    uname.send_keys(username)
    email1.send_keys(email)
    time.sleep(0.6)
    passwd.send_keys(password)
    passwd1.send_keys(confirm_password)
    print(3)
    time.sleep(1)
    login_button.click()


@then(u'she should see a message of Password and confirm password are not the same')
def see_register_failure4(context):
    time.sleep(0.4)
    flaskr_found = re.search("Password and confirm password are not the same", context.browser.page_source, re.IGNORECASE)
    assert flaskr_found


@then(u'she should see a message of Not a Valid Password')
def see_register_failure3(context):
    time.sleep(0.4)
    flaskr_found = re.search("Not a Valid Password", context.browser.page_source, re.IGNORECASE)
    assert flaskr_found


# @then(u'she should see a message of User name has already existed, please try again')
# def see_register_failure1(context):
#     time.sleep(0.4)
#     flaskr_found = re.search("User name has already existed, please try again", context.browser.page_source, re.IGNORECASE)
#     assert flaskr_found


@then(u'she turns to show_entries')
def see_register_failure2(context):
   pass

@then(u'she should see the name field')
def see_name(context):
    flaskr_found = re.search("name", context.browser.page_source, re.IGNORECASE)
    assert flaskr_found

@When(u'she clicks on the Register link')
def register_page(context):
    register_found=context.browser.find_element_by_link_text("Sign up")
    register_found.click()

@then(u'she turns to register page')
def register_page(context):
    pass


