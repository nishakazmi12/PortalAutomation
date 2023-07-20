import time

import pytest

from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customerLogger import LogGen
from utilities import excelUtility
from pageObjects.HomePage import HomePage


class Test_002_Login:
    # Access Local Data
    baseUrl = ReadConfig.getApplicationURL()
    port = ReadConfig.getPort()
    path = ".//TestData/devPortal_LoginTestData.xlsx"
    # Logging Object
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_loginPage(self, setup):
        self.logger.info("*************** Test_002_Login *****************")
        self.logger.info("**** Started Login DDR test ****")
        self.driver = setup
        self.logger.info("****Opening URL****")

        #  self.driver.get(self.baseUrl+'login')
        self.driver.get(self.baseUrl)

        # create login page object
        self.login_page_obj = LoginPage(self.driver)

        # TODO = url resolver check issue need to refactor after resolver issue resolved!
        self.login_page_obj.setPort(self.port)
        self.login_page_obj.clickConnect()
        time.sleep(1)
        self.logger.info("****Server Connected to Portal****")

        # Find num of rows in Excel file
        self.rows = excelUtility.getRowCount(self.path, 'Sheet1')
        print("Num of Rows in Excel Sheet ", self.rows)

        # Expected Output Array
        lst_status = []

        for r in range(2, self.rows + 1):
            self.username = excelUtility.readData(self.path, 'Sheet1', r, 1)
            self.password = excelUtility.readData(self.path, 'Sheet1', r, 2)
            self.expected = excelUtility.readData(self.path, 'Sheet1', r, 3)

            self.login_page_obj.setUserName(self.username)
            self.login_page_obj.setPassword(self.password)
            self.login_page_obj.clickLogin()

            time.sleep(1)

            current_url = self.driver.current_url
            if current_url == "http://localhost:3000/home":
                if self.expected == 'Pass':
                    self.logger.info("**** passed ****")
                    lst_status.append("Pass")
                    self.home_page_object = HomePage(self.driver)
                    self.home_page_object.clickSignOut()
                    self.login_page_obj.setPort(self.port)
                    self.login_page_obj.clickConnect()

                elif self.expected == 'Fail':
                    self.logger.info("**** failed ****")
                    lst_status.append("Fail")

            elif current_url != "http://localhost:3000/home":
                if self.expected == 'Pass':
                    self.logger.info("**** failed ****")
                    lst_status.append("Fail")
                elif self.expected == 'Fail':
                    self.logger.info("**** passed ****")
                    lst_status.append("Pass")
        print(lst_status)

        if "Fail" not in lst_status:
            self.logger.info("******* DDT Login test passed **********")
            self.driver.close()
            assert True
        else:
            self.logger.error("******* DDT Login test failed **********")
            self.driver.close()
            assert False

        self.logger.info("******* End of Login DDT Test **********")
        self.logger.info("**************** Completed  TC_LoginDDT_002 ************* ")
