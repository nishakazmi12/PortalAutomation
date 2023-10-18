# Define / execute all page test case from here

import unittest
from selenium import webdriver
import page
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locator import *
from sourcefiles import *
from webdriver_manager.chrome import ChromeDriverManager
import time
import class_Login
import tracemalloc

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService



class PortalSignUp(unittest.TestCase):

    #Create a setUp function as unittest.TestCase needs this to setup the variables and configuration.
    # Similar to __init__
    def setUp(self):

        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/")
        tracemalloc.start()

    # Any function which starts with "test" + any keyword. This method will automatically run when we run the unittest.
    # Otherwise, any method not starting with the word test, won't auto-run.
    def title(self):

        # Test 01 Connect to Server
        SignUpPage = page.SignUpPage(self.driver)
        SignUpPage.set_up("HTTPS://LOCALHOST", "9263")
        SignUpPage.signup_page()

        # Test 01 Web Page Title
        # assert, see if the condition on the right side is true. If true then test case pass.

        assert SignUpPage.is_portal_signup_title_matches() == "User Registration"


    def sign_up(self):

        SignUpPage = page.SignUpPage(self.driver)
        SignUpPage.set_up("HTTPS://LOCALHOST", "9263")
        SignUpPage.signup_page()

        SignUpPage.enter_user_register_data("noni", "kazmi", "abc",
                                            "noni", "nishakazmi@hotmail.com", "Astera123",
                                            "Astera123")

        #SignUpPage.enter_user_register_data("m", "Saad", "abc",
        #                                    "mSaad", "mSaad@astera.com", "Astera123",
        #                                    "Astera123")


    def signup_via_file_success(self):

        SignUpPage = page.SignUpPage(self.driver)
        SignUpPage.set_up("HTTPS://LOCALHOST", "9263")
        SignUpPage.signup_page()
        SignUpPage.enter_signup_data_via_file(source_file().csv_filepath_valid_signUp_credentials)



    def signup_via_file_fail(self):

        SignUpPage = page.SignUpPage(self.driver)
        SignUpPage.set_up("HTTPS://LOCALHOST", "9263")
        SignUpPage.signup_page()
        SignUpPage.enter_signup_data_via_file(source_file().csv_filepath_invalid_signUp_credentials)



    def signup_fields_verification(self):

        SignUpPage = page.SignUpPage(self.driver)
        SignUpPage.set_up("HTTPS://LOCALHOST", "9263")
        SignUpPage.signup_page()
        SignUpPage.verify_signup_fields("a", "a", "a", "a", "a", "a", "df")


    def test_signup_email_verification(self):

        self.driver.quit()
        SignUpPage = page.SignUpPage(self.driver)
        #SignUpPage.set_up("HTTPS://LOCALHOST", "9263")
        #SignUpPage.signup_page()
        SignUpPage.verification_signup_email("smtp-mail.outlook.com", "", "", 'SUBJECT "Astera Email Confirmation Link"')

        SignUpPage.verify_validate_signup("noni", "Astera123")


    def signup_verification_timetolive(self):

        SignUpPage = page.SignUpPage(self.driver)
        SignUpPage.set_up("HTTPS://LOCALHOST", "9263")
        SignUpPage.signup_page()

        # Call the Sign Up method
        SignUpPage.sign_up()

        # Implicit wait for the link verification
        self.driver.implicitly_wait(1.86e+6)

        # fetching and browsing the link from the email content
        SignUpPage.verification_signup_email("imap-mail.outlook.com", "your_email@hotmail.com", "password",
                                  'SUBJECT "Astera Email Confirmation Link"')



    #Run after the test case(s) is/are finished, needed by unittest.TestCase
    def tearDown(self):

        input("Press any key to quit...")
        self.driver.close()

# Run the main file using the module unittest
if __name__ == "__main__":
    unittest.main()


