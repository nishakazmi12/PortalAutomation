import pytest
from selenium import webdriver
import time
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customerLogger import LogGen

class Test_001_Login:

    # Access Local Data
    baseUrl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    port = ReadConfig.getPort()

    # Logging Object
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_homePageTitle(self, setup):
        self.logger.info("*************** Test_001_Login *****************")
        self.logger.info("**** Started Home page title test ****")
        self.driver = setup
        self.logger.info("****Opening URL****")
        self.driver.get(self.baseUrl)
        acc_title = self.driver.title
        if acc_title == "Developer Portal":
            self.logger.info("**** Home page title test passed ****")
            self.driver.close()
            assert True
        else:
            self.logger.error("**** Home page title test failed****")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
            self.logger.info("**** ScreenShoot captured ****")
            self.driver.close()
            assert False



    @pytest.mark.sanity
    def test_connectPage(self, setup):
        self.logger.info("**** Started Connect Server test ****")
        self.driver = setup
        self.logger.info("****Opening URL****")
        self.driver.get(self.baseUrl)

        # create login page object

        self.login_page_obj = LoginPage(self.driver)
        self.logger.info("****Setting Port Number****")
        self.login_page_obj.setPort(self.port)
        self.logger.info("****Connect Button Clicked****")
        self.login_page_obj.clickConnect()
        self.logger.info("****Check Login Tag****")
        element = self.login_page_obj.checkLoginPage()
        if element:
            self.logger.info("****Connect to Server Test Pass****")
            self.driver.close()
            assert True
        else:
            self.logger.error("****Connect to Server Test Fail****")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_connectPage.png")
            self.logger.info("**** ScreenShoot captured ****")
            self.driver.close()
            assert False

    @pytest.mark.regression
    def test_loginPage(self, setup):
        self.logger.info("**** Started Login test ****")
        self.driver = setup
        self.logger.info("****Opening URL****")

        #  self.driver.get(self.baseUrl+'login')
        self.driver.get(self.baseUrl)

        # create login page object
        self.login_page_obj = LoginPage(self.driver)

        # TODO = url resolver check issue need to refactor after resolver issue resolved!
        self.login_page_obj.setPort(self.port)
        self.login_page_obj.clickConnect()
        time.sleep(3)
        self.logger.info("****Server Connected to Portal****")

        self.login_page_obj.setUserName(self.username)
        self.logger.info("****Setting username****")

        time.sleep(3)

        self.login_page_obj.setPassword(self.password)
        time.sleep(3)
        self.logger.info("****Setting password****")

        self.login_page_obj.clickLogin()
        self.logger.info("****Requesting to Login****")

        time.sleep(3)
        self.logger.info("****Retrieving Current URL****")

        current_url = self.driver.current_url
        if current_url == "http://localhost:3000/home":
            self.logger.info("****Login Test Passed****")
            self.driver.close()
            assert True
        else:
            self.logger.error("****Login Test Failed****")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_loginPage.png")
            self.logger.info("**** ScreenShoot captured ****")
            self.driver.close()
            assert False
