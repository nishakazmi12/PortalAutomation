import time
import pytest

from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customerLogger import LogGen
from pageObjects.HomePage import HomePage


class Test_002_Home:
    # Access Local Data
    baseUrl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    port = ReadConfig.getPort()

    # Logging Object
    logger = LogGen.loggen()

    def login_setup_code(self, setup):

        self.driver = setup
        #  self.driver.get(self.baseUrl+'login')
        self.driver.get(self.baseUrl)

        # create login page object
        self.login_page_obj = LoginPage(self.driver)
        self.login_page_obj.setPort(self.port)
        self.login_page_obj.clickConnect()

        time.sleep(1)

        self.login_page_obj.setUserName(self.username)
        self.login_page_obj.setPassword(self.password)
        self.login_page_obj.clickLogin()

        time.sleep(1)


    # Subscription
    @pytest.mark.subs
    def test_heading_subscribe(self, setup):

        self.login_setup_code(setup)
        self.home_page_obj = HomePage(self.driver)
        self.home_page_obj.subscribe_page_button()
        assert self.driver.current_url == "http://localhost:3000/home"


    #@pytest.mark.subs
    def test_swagger_of_product(self, setup):

        self.login_setup_code(setup)
        self.home_page_obj = HomePage(self.driver)
        self.home_page_obj.click_on_subscribe_button()

        #Go to client during this sleep time and grant/deny the access to the user.
        time.sleep(7)

        self.home_page_obj.subscribe_page_button()
        time.sleep(2)
        self.home_page_obj.expand_subscribe_product()
        time.sleep(2)
        self.driver.fullscreen_window()
        time.sleep(2)
        self.home_page_obj.click_on_swagger_button()
        time.sleep(3)

        assert self.home_page_obj.title_of_swagger_ui() == "Swagger UI"

    #@pytest.mark.subs
    def test_open_product_swagger_in_browser(self, setup):

        self.login_setup_code(setup)
        self.home_page_obj = HomePage(self.driver)
        #Pre-condition - A product should already be subscribed.
        self.home_page_obj.subscribe_page_button()
        time.sleep(2)
        self.home_page_obj.expand_subscribe_product()
        time.sleep(2)
        self.driver.fullscreen_window()
        time.sleep(2)
        self.home_page_obj.click_on_swagger_button()
        time.sleep(2)

        #open URL in a browser tab.
        #match title of the tab
        self.home_page_obj.return_open_swagger_URL()


    #@pytest.mark.subs
    def test_call_endpoint_on_swagger(self, setup):

        self.login_setup_code(setup)
        self.home_page_obj = HomePage(self.driver)
        self.home_page_obj.subscribe_page_button()
        time.sleep(2)
        self.home_page_obj.expand_subscribe_product()
        time.sleep(2)
        self.driver.fullscreen_window()
        time.sleep(2)
        self.home_page_obj.click_on_swagger_button()
        time.sleep(2)

        assert self.home_page_obj.perform_endpoint_call("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9uYW1laWRlbnRpZmllciI6IjEiLCJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9lbWFpbGFkZHJlc3MiOiJhZG1pbkBjZW50ZXJwcmlzZS5jb20iLCJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9uYW1lIjoiYWRtaW4iLCJzdWIiOiJhZG1pbiIsImp0aSI6ImU2M2FjNTFhLTFlOTItNGE2My1hNzJiLWIyNWJkZjViMGVmNSIsImlhdCI6MTY4ODU0OTEyMSwicm9sIjoiYXBpX2FjY2VzcyIsImlkIjoiMSIsIm5iZiI6MTY4ODU0OTEyMCwiZXhwIjoxNjkxMTQxMTIwfQ.Gdozwdu5hXYJG5qF-ip9Kssl50hVLQ_gEoIDwUULKR0",
                                                   "1") == "200"

   # @pytest.mark.subs
    def test_call_endpoint_on_swagger_invalid(self, setup):

        self.login_setup_code(setup)
        self.home_page_obj = HomePage(self.driver)
        self.home_page_obj.subscribe_page_button()
        self.home_page_obj.expand_subscribe_product()
        self.driver.fullscreen_window()
        time.sleep(2)
        self.home_page_obj.click_on_swagger_button()
        time.sleep(3)

        assert self.home_page_obj.perform_endpoint_call("inalid_token", "1") != "200"





