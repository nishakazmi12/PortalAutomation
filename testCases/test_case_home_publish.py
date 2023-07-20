import time
import pytest
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customerLogger import LogGen
from pageObjects.HomePage import HomePage


class Test_001_Home:
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

    # Published
    # pytest -v -s -m="unit"  testCases/ --browser chrome
    @pytest.mark.publish
    def test_publishPage_URL(self, setup):
        self.login_setup_code(setup)
        assert self.driver.current_url == "http://localhost:3000/home"

    # @pytest.mark.publish
    def test_heading_publish(self, setup):
        self.login_setup_code(setup)
        self.home_page_obj = HomePage(self.driver)
        self.home_page_obj.publish_page_button()

        assert self.home_page_obj.publish_page_heading() == "Welcome to Developer Portal"

    # @pytest.mark.publish
    def test_subscribe_to_product(self, setup):
        self.login_setup_code(setup)
        self.home_page_obj = HomePage(self.driver)
        self.home_page_obj.click_on_subscribe_button()
        time.sleep(2)

        assert self.home_page_obj.notification_of_subscribe_request() == "Request Submitted"

    # Not tested yet
    @pytest.mark.publish
    def test_subscribe_button_disable(self, setup):
        self.login_setup_code(setup)
        self.home_page_obj = HomePage(self.driver)
        self.home_page_obj.click_on_subscribe_button()
        time.sleep(2)
        success = self.home_page_obj.notification_of_subscribe_request()
        time.sleep(5)
        failure = self.home_page_obj.click_on_subscribe_disable_button()

        assert success == "Request Submitted" and failure == "Subscription Requested"
