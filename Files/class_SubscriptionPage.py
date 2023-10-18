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
        loginPage.enter_credentials("noni", "Astera123")


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

        assert subscribePage.perform_endpoint_call("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9uYW1laWRlbnRpZmllciI6IjEiLCJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9lbWFpbGFkZHJlc3MiOiJhZG1pbkBjZW50ZXJwcmlzZS5jb20iLCJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9uYW1lIjoiYWRtaW4iLCJzdWIiOiJhZG1pbiIsImp0aSI6ImU2M2FjNTFhLTFlOTItNGE2My1hNzJiLWIyNWJkZjViMGVmNSIsImlhdCI6MTY4ODU0OTEyMSwicm9sIjoiYXBpX2FjY2VzcyIsImlkIjoiMSIsIm5iZiI6MTY4ODU0OTEyMCwiZXhwIjoxNjkxMTQxMTIwfQ.Gdozwdu5hXYJG5qF-ip9Kssl50hVLQ_gEoIDwUULKR0",
                                                   "1") == "200"



    def tearDown(self):

        input("Press any key to quit...")
        self.driver.close()


# Run the main file using the module unittest
if __name__ == "__main__":
    unittest.main()

