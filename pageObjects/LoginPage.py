from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    # Locators for Connect Page
    text_box_port_id = "Port"
    icon_loginActive_xpath = "//body/div[@id='root']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]"
    button_connect_xpath = "//body/div[@id='root']/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[" \
                           "3]/div[1]/div[1]/div[1]/div[1]/button[1]"
    icon_server_class = "ant-steps-item ant-steps-item-process ant-steps-item-active"

    # Locators for Login Page
    text_box_username_xpath = "//input[@id='User']"
    text_box_password_id = "Password"
    button_login_xpath = "//span[contains(text(),'LOGIN')]"


    def __init__(self, driver):
        self.driver = driver

    # Connect page functions

    def setPort(self, port):
        port_element = self.driver.find_element(By.ID, self.text_box_port_id)
        port_element.send_keys(Keys.CONTROL + "a")  # Select all the existing text
        port_element.send_keys(Keys.DELETE)  # Delete the selected text
        port_element.send_keys(port)  # Enter the new value

    def clickConnect(self):
        self.driver.find_element(By.XPATH, self.button_connect_xpath).click()

    def checkLoginPage(self):
        # TODO-> We can optimize this function later
        element = self.driver.find_element(By.XPATH, self.icon_loginActive_xpath)
        if element != "":
            return True
        else:
            return False

    # Login Page Function
    def setUserName(self, username):

        self.driver.find_element(By.XPATH, self.text_box_username_xpath).clear()
        self.driver.find_element(By.XPATH, self.text_box_username_xpath).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.ID, self.text_box_password_id).clear()
        self.driver.find_element(By.ID, self.text_box_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()
