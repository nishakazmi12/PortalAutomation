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

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService



# One Class for one feature
class PortalLogin(unittest.TestCase):


    def setUp(self):
        #self.driver = webdriver.Chrome(service_log_path="C:\Program Files (x86)\chromedriver.exe")
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        #self.driver = webdriver.Chrome(executable_path="C:\Program Files (x86)\chromedriver.exe")
        #self.driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
        self.driver.get("http://localhost:3000/")
        # http://localhost:3000/home and http://localhost:3000/login both URLs are not working yet.

    def title(self):

        loginPage = page.LoginPage(self.driver)

        # Test 01 Web Page Title
        assert loginPage.is_portal_title_matches()

        # Test 02 Connect to Server
        loginPage.connect_server("HTTPS://LOCALHOST","9263")

        # assert WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(LoginPageLocators.Login_Active))
        # To DO -> need to change this assert method

        # assert self.driver.current_url == currentLoginURL

    # Need to call test_title first
    def login(self):

        loginPage = page.LoginPage(self.driver)
        loginPage.connect_server("HTTPS://LOCALHOST", "9263")

        # Test 01 Simple Login
        loginPage.enter_credentials("noni", "Astera123")

        # https://stackoverflow.com/questions/45347675/make-selenium-wait-10-seconds
        assert self.driver.current_url == "http://localhost:3000/home"


        # Add sign out code
        # http://localhost:3000/home

    # Need to call test_title first
    def login_via_file_success(self):

        loginPage = page.LoginPage(self.driver)
        loginPage.connect_server("HTTPS://LOCALHOST", "9263")


        # Test 02 Login Using Valid Data
        loginPage.enter_credentials_via_file(source_file().csv_filepath_valid_credentials)
        # Sign out code added
        # Look into this after signout do we go to the login page or home page

    # Need to call test_title first
    def login_via_file_fail(self):

        loginPage = page.LoginPage(self.driver)
        loginPage.connect_server("HTTPS://LOCALHOST", "9263")

        # Test 03 Login Using Invalid Data
        loginPage.enter_credentials_via_file(source_file().csv_filepath_invalid_credentials)


    def tearDown(self):

        input("Press any key to quit...")
        self.driver.close()


# Run the main file using the module unittest
if __name__ == "__main__":
    unittest.main()



# The procedure of method is setUp, testcase1, teardown then again setup, testcase2, teardown.
# This is the sequence