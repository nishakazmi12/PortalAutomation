import time
import pytest
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customerLogger import LogGen
from testCases.test_case_login import Test_001_Login
from pageObjects.HomePage import HomePage


class Test_004_Home:
    # Access Local Data
    baseUrl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    port = ReadConfig.getPort()

    # Logging Object
    logger = LogGen.loggen()
    # TODO Refactor this function dont need to repeat test case function

    @pytest.mark.regression
    def test_signOut(self, setup):

        self.driver = setup

        #  self.driver.get(self.baseUrl+'login')
        self.driver.get(self.baseUrl)

        # create login page object
        self.login_page_obj = LoginPage(self.driver)

        # TODO = url resolver check issue need to refactor after resolver issue resolved!
        self.login_page_obj.setPort(self.port)
        self.login_page_obj.clickConnect()
        time.sleep(1)

        self.login_page_obj.setUserName(self.username)

        self.login_page_obj.setPassword(self.password)
        self.login_page_obj.clickLogin()

        time.sleep(1)

        current_url = self.driver.current_url
        if current_url == "http://localhost:3000/home":
            self.logger.info("****Login Successfully***")
            self.home_page_object = HomePage(self.driver)
            self.home_page_object.clickSignOut()
            time.sleep(2)
            login_url = self.driver.current_url
            if login_url == "http://localhost:3000/login":
                self.logger.info("****Logout Successfully***")
                self.driver.close()
                assert True
            else:
                self.logger.error("****Logout  Failed****")
                self.driver.save_screenshot(".\\Screenshots\\" + "test_logout.png")
                self.logger.info("**** ScreenShoot captured ****")
                self.driver.close()
                assert False
        else:
            self.logger.error("****Login  Failed****")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_loginPage.png")
            self.logger.info("**** ScreenShoot captured ****")
            self.driver.close()
            assert False
