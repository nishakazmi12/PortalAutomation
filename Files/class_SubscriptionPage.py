# Define / execute all page test case from here

import unittest
import page
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locator import *
from sourcefiles import *
import time
import class_Login


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


class PortalSubscriptionPage(unittest.TestCase):

    # Similar to __init__
    def setUp(self):

        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/")
        self.driver.fullscreen_window()
        loginPage = page.LoginPage(self.driver)
        loginPage.connect_server("HTTPS://LOCALHOST", "9263")
        loginPage.enter_credentials("name", "password")


    def subscribePage_URL(self):

        assert self.driver.current_url == "http://localhost:3000/home"


    def heading_subscribe(self):

        subscribePage = page.SubscriptionPage(self.driver)
        subscribePage.subscribe_page_button()


    def swagger_of_product(self):

        publishPage = page.PublishedPage(self.driver)
        publishPage.click_on_subscribe_button()

        #Go to client during this sleep time and grant/deny the access to the user.
        time.sleep(7)

        subscribePage = page.SubscriptionPage(self.driver)
        subscribePage.subscribe_page_button()
        subscribePage.click_on_swagger_button()


        assert subscribePage.title_of_swagger_ui() == "Swagger UI"

    def open_product_swagger_in_browser(self):

        #Pre-condition - A product should already be subscribed.
        subscribePage = page.SubscriptionPage(self.driver)
        subscribePage.subscribe_page_button()
        subscribePage.click_on_swagger_button()

        #open URL in a browser tab.
        #match title of the tab
        subscribePage.return_open_swagger_URL()

    def test_call_endpoint_on_swagger(self):

        subscribePage = page.SubscriptionPage(self.driver)
        subscribePage.subscribe_page_button()
        subscribePage.click_on_swagger_button()

        assert subscribePage.perform_endpoint_call("Authentication Token",
                                                   "1") == "200"



    def tearDown(self):

        input("Press any key to quit...")
        self.driver.close()


# Run the main file using the module unittest
if __name__ == "__main__":
    unittest.main()

