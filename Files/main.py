# Define / execute all page test case from here 

import unittest
from selenium import webdriver
import page
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locator import *
from sourcefiles import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService



# One Class for one feature
class PortalLogin(unittest.TestCase):

    def setUp(self):


        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        #self.driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
        self.driver.get("http://vmqa516:9362/")
        self.currentURL = "http://vmqa516:9362"
    

    def test_title(self):

        loginPage = page.LoginPage(self.driver)

        # Test 01 Web Page Title
        assert loginPage.is_portal_title_matches()

        # Test 02 Connect to Server
        loginPage.connect_server("https://vmqa516","9262")

        # assert WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(LoginPageLocators.Login_Active))
        # To DO -> need to change this assert method

        # assert self.driver.current_url == currentLoginURL

    # Need to call test_title first
    def login(self):

        # Test 01 Login Page
        loginPage.enter_credentials("Admin", "Admin123")
        assert self.driver.current_url == (currentURL + "/login")
        # Add sign out code
        # http://localhost:3000/home

    # Need to call test_title first
    def login_via_file_success(self):

        # Test 02 Login Using Valid Data
        loginPage.enter_credentials_via_file(csv_filepath_valid_credentials)
        # Sign out code added
        # Look into this after signout do we go to the login page or home page

    # Need to call test_title first
    def login_via_file_fail(self):

        # Test 03 Login Using Invalid Data
        loginPage.enter_credentials_via_file(csv_filepath_invalid_credentials)


    def tearDown(self):

        input("Press any key to quit...")
        self.driver.close()

'''

# Separate this loc to another file.
class PortalSignUp(unittest.TestCase):

    #Create a setUp function as unittest.TestCase needs this to setup the variables and configuration.
    # Similar to __init__
    def setUp(self):

        self.driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
        self.driver.get("http://localhost:9362/")
        self.currentURL = "http://localhost:9362"  # Making this dynamic
        # self.currentLoginURL = self.driver.current_url
        # http://localhost:9362/home and http://localhost:9362/singup both URLs are not working yet.
        SignUpPage = page.SignUpPage(self.driver)

        # Test 01 Connect to Server
        SignUpPage.set_up("9263")
        signup_page()

    # Any function which starts with "test" + any keyword. This method will automatically run when we run the unittest.
    # Otherwise, any method not starting with the word test, won't auto-run.
    def test_title(self):

        # Test 01 Web Page Title
        # assert, see if the condition on the right side is true. If true then test case pass.
        assert SignUpPage.is_portal_title_matches()


    def sign_up(self):

        SignUpPage.enter_user_register_data("name", "lastname", "middlename",
                                            "username", "emailaddress", "password",
                                            "confirmpassword")


    def signup_via_file_success(self):

        SignUpPage.enter_signup_data_via_file(csv_filepath_valid_signUp_credentials)



    def signup_via_file_fail(self):

        SignUpPage.enter_signup_data_via_file(csv_filepath_invalid_signUp_credentials)



    def signup_fields_verification(self):

        SignUpPage.verify_signup_fields("name", "lastname", "middlename",
                                            "username", "emailaddress", "password",
                                            "confirmpassword")


    def signup_email_verification(self):

        SignUpPage.verification_signup_email("imap-mail.outlook.com", "your_email@hotmail.com", "password", 'SUBJECT "Astera Email Confirmation Link"')

        SignUpPage.verify_validate_signup("username", "password")


    def signup_verification_timetolive(self):

        # Caal the Sign Up method
        sign_up()

        # Implicit wait for the link verification
        self.driver.implicitly_wait(1.86e+6)

        # fetching and browsing the link from the email content
        SignUpPage.verification_signup_email("imap-mail.outlook.com", "your_email@hotmail.com", "password",
                                  'SUBJECT "Astera Email Confirmation Link"')



    #Run after the test case(s) is/are finished, needed by unittest.TestCase
    def tearDown(self):

        input("Press any key to quit...")
        self.driver.close()


'''


# Run the main file using the module unittest
if __name__ == "__main__":
    unittest.main()



# The procedure of method is setUp, testcase1, teardown then again setup, testcase2, teardown.
# This is the sequence
