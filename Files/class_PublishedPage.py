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


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService



class PortalPublishedPage(unittest.TestCase):

    # Similar to __init__
    def setUp(self):

        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/")
        loginPage = page.LoginPage(self.driver)
        loginPage.connect_server("HTTPS://LOCALHOST", "9263")
        loginPage.enter_credentials("noni", "Astera123")


    def publishPage_URL(self):

        assert self.driver.current_url == "http://localhost:3000/home"

    def heading_publish(self):

        publishPage = page.PublishedPage(self.driver)
        publishPage.publish_page_button()

        assert publishPage.publish_page_heading() == "Welcome to Developer Portal"

    def test_subscribe_to_product(self):

        publishPage = page.PublishedPage(self.driver)
        publishPage.click_on_subscribe_button()

        print(publishPage.notification_of_subscribe_request())
        assert publishPage.notification_of_subscribe_request() == "Request Submitted"


    def tearDown(self):

        input("Press any key to quit...")
        self.driver.close()


# Run the main file using the module unittest
if __name__ == "__main__":
    unittest.main()

