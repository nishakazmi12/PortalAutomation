import time
import pytest
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customerLogger import LogGen
from testCases.test_case_login import Test_001_Login
from pageObjects.SignupPage import SignupPage
from pageObjects.SignupPage import SignupPage


class Test_001_Signout:
    # Access Local Data
    baseUrl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    port = ReadConfig.getPort()

    name_signup = ReadConfig.getFirstnameSignup()
    lastname_signup = ReadConfig.getLastnameSignup()
    middlename_signup = ReadConfig.getMiddlenameSignup()
    username_signup = ReadConfig.getUsernameSignup()
    emailaddress_signup = ReadConfig.getEmailSignup()
    password_signup = ReadConfig.getPasswordSignup()
    confirmpassword_signup = ReadConfig.getConfirmPassword()

    email_server = ReadConfig.getEmailServer()
    email_port = ReadConfig.getEmailPort()
    email_address = ReadConfig.getEmailEmailAdd()
    email_password = ReadConfig.getEmailPassword()
    email_subject = ReadConfig.getEmailSubject()

    invalid_path = ".//TestData/SignUpCredentials_Invalid.csv"
    valid_path = ".//TestData/SignUpCredentials_Valid.csv"

    # Logging Object
    logger = LogGen.loggen()

    def test_connectPage(self, setup):
        self.logger.info("**** Started Connect Server test ****")
        self.driver = setup
        self.logger.info("****Opening URL****")
        self.driver.get(self.baseUrl)

        # create login page object
        self.login_page_obj = LoginPage(self.driver)
        self.login_page_obj.setPort(self.port)
        self.login_page_obj.clickConnect()

        time.sleep(1)
        # self.login_page_obj = LoginPage(self.driver)
        # self.logger.info("****Setting Port Number****")
        # self.login_page_obj.setPort(self.port)
        # self.logger.info("****Connect Button Clicked****")
        # self.login_page_obj.clickConnect()

    # TODO Refactor this function dont need to repeat test case function

    #@pytest.mark.sign
    def test_title(self, setup):

        self.test_connectPage(setup)
        self.signup_page_obj = SignupPage(self.driver)
        self.signup_page_obj.signup_page_button()
        time.sleep(3)
        assert self.signup_page_obj.is_portal_signup_title_matches() == "User Registration"

    #@pytest.mark.sign
    def test_sign_up(self, setup):

        self.test_connectPage(setup)
        self.signup_page_obj = SignupPage(self.driver)
        self.signup_page_obj.signup_page_button()
        self.signup_page_obj.enter_user_register_data(self.name_signup, self.lastname_signup, self.middlename_signup,
                                            self.username_signup, self.emailaddress_signup, self.password_signup,
                                            self.confirmpassword_signup)

    #@pytest.mark.sign
    def test_signup_via_file_success(self, setup):

        self.test_connectPage(setup)
        self.signup_page_obj = SignupPage(self.driver)
        self.signup_page_obj.signup_page_button()
        self.signup_page_obj.enter_signup_data_via_file(self.valid_path)

    #@pytest.mark.sign
    def test_signup_via_file_fail(self, setup):

        self.test_connectPage(setup)
        self.signup_page_obj = SignupPage(self.driver)
        self.signup_page_obj.signup_page_button()
        self.signup_page_obj.enter_signup_data_via_file(self.invalid_path)

    #@pytest.mark.sign
    def test_signup_fields_verification(self, setup):

        self.test_connectPage(setup)
        self.signup_page_obj = SignupPage(self.driver)
        self.signup_page_obj.signup_page_button()
        self.signup_page_obj.verify_signup_fields("a", "a", "a", "a", "a", "a", "df")

    @pytest.mark.sign
    def test_signup_email_verification(self, setup):

        self.test_connectPage(setup)
        self.signup_page_obj = SignupPage(self.driver)
        verification_signup_email_element = self.signup_page_obj.verification_signup_email(self.email_server, self.email_port, self.email_address, self.email_password, self.email_subject)
        self.signup_page_obj.verify_validate_signup(verification_signup_email_element, self.username_signup, self.password_signup)

    # @pytest.mark.sign
    def test_signup_verification_timetolive(self, setup):

        self.test_sign_up(setup)
        # Implicit wait for the link verification
        self.driver.implicitly_wait(1.86e+6)

        # fetching and browsing the link from the email content
        self.signup_page_obj.verification_signup_email(self.email_server, self.email_address, self.email_password, self.email_subject)


