from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class HomePage:
    # Locator for HomePage
    button_sighOut_xpath = "//body/div[@id='root']/section[1]/section[1]/aside[1]/div[1]/ul[1]/li[4]"

    # Publish Locators
    click_publishdpage_button_xpath = "//body/div[@id='root']/section[1]/section[1]/aside[1]/div[1]/ul[1]/li[1]"
    heading_publishedpage_xpath = "//h1[contains(text(),'Welcome to Developer Portal')]"
    subscribe_expand_publishedpage_xpath = "//body/div[@id='root']/section[1]/section[1]/main[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]"
    subscribe_button_publishedpage_xpath = "//body/div[@id='root']/section[1]/section[1]/main[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/button[1]"
    successful_request_notification_xpath = "//div[@class='ant-notification-notice-message']"
    subscribe_button_disable_xpath = "//body/div[@id='root']/section[1]/section[1]/main[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/button[1]"

    # Locators for Subscription
    click_subscribepage_button = "//body/div[@id='root']/section[1]/section[1]/aside[1]/div[1]/ul[1]/li[2]"
    subscribe_expand_subscribepage = "//body/div[@id='root']/section[1]/section[1]/main[1]/div[2]/div[1]/div[1]/div[1]/div[1]"
    swagger_button_subscribepage = "//body/div[@id='root']/section[1]/section[1]/main[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/button[1]"
    title_swagger = "//body/div[3]/div[1]/div[2]/div[1]/div[2]/div[1]"
    URL_swagger = "//body/div[3]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/section[1]/div[1]/div[1]/hgroup[1]/a[1]/span[1]"
    authorize_button = "div.ant-modal-root div.ant-modal-wrap div.ant-modal div.ant-modal-content:nth-child(2) div.ant-modal-body div.swagger-ui div:nth-child(2) div.scheme-container:nth-child(2) section.schemes.wrapper.block.col-12 div.auth-wrapper:nth-child(2) > button.btn.authorize.unlocked"
    auth_textbox = "//input[@aria-label='auth-bearer-value']"
    token_auth_button = "//button[contains(text(),'Authorize')]"
    auth_close_button = "//button[contains(text(),'Close')]"
    Auth_Logout_Button = "//button[contains(text(),'Logout')]"
    expand_endpoint = "//body/div[3]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[2]/div[4]/section[1]/div[1]/span[1]/div[1]/div[1]/div[1]/span[1]/div[1]/div[1]/button[1]"
    try_it_out_button = "//button[contains(text(),'Try it out')]"
    parameter_product_id = "//tbody/tr[1]/td[2]/input[1]"
    execute = "//button[contains(text(),'Execute')]"
    response_status_code = "//body[1]/div[3]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[2]/div[4]/section[1]/div[1]/span[1]/div[1]/div[1]/div[1]/span[1]/div[1]/div[2]/div[1]/div[4]/div[2]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[1]"

    def __init__(self, driver):
        self.url_element = None
        self.driver = driver

    def clickSignOut(self):
        self.driver.find_element(By.XPATH, self.button_sighOut_xpath).click()

    # Publish
    def publish_page_button(self):
        self.driver.find_element(By.XPATH, self.click_publishdpage_button_xpath).click()


    def publish_page_heading(self):
        heading_publishedpage_element = self.driver.find_element(By.XPATH, self.heading_publishedpage_xpath)
        return heading_publishedpage_element.text

    def click_on_subscribe_button(self):
        self.driver.find_element(By.XPATH, self.subscribe_expand_publishedpage_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.subscribe_button_publishedpage_xpath).click()


    def click_on_subscribe_disable_button(self):
        subscribe_button_disable_xpath_element = self.driver.find_element(By.XPATH, self.subscribe_button_disable_xpath)
        subscribe_button_disable_xpath_element.click()

        return subscribe_button_disable_xpath_element.text


    def notification_of_subscribe_request(self):
        successful_request_notification_element = self.driver.find_element(By.XPATH, self.successful_request_notification_xpath)
        print(successful_request_notification_element.text)
        return successful_request_notification_element.text

    # Subscribe
    def subscribe_page_button(self):
        self.driver.find_element(By.XPATH, self.click_subscribepage_button).click()
        time.sleep(2)


    def expand_subscribe_product(self):
        self.driver.find_element(By.XPATH, self.subscribe_expand_subscribepage).click()


    def click_on_swagger_button(self):
        self.driver.find_element(By.XPATH, self.swagger_button_subscribepage).click()


    def title_of_swagger_ui(self):
        return self.driver.find_element(By.XPATH, self.title_swagger).text


    def return_open_swagger_URL(self):

        try:
            url_element = self.driver.find_element(By.XPATH, self.URL_swagger)
            url_element.get_attribute('href')
            time.sleep(3)
            url_element.click()
            time.sleep(3)
            print(url_element.text)

            #assert url_element == self.driver.current_url
            assert url_element.text != self.driver.current_url

        except ValueError:
            print(ValueError)


    def perform_endpoint_call(self, bearerToken, productID):

        try:
            self.driver.find_element(By.CSS_SELECTOR, self.authorize_button).click()
            time.sleep(3)

            textbox_auth_element = self.driver.find_element(By.XPATH, self.auth_textbox)
            textbox_auth_element.send_keys(Keys.CONTROL + "a")  # Select all the existing text
            textbox_auth_element.send_keys(Keys.DELETE)  # Delete the selected text
            textbox_auth_element.send_keys(bearerToken)  # Enter the new value

            self.driver.find_element(By.XPATH, self.token_auth_button).click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, self.auth_close_button).click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, self.expand_endpoint).click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, self.try_it_out_button).click()
            time.sleep(2)

            if productID is not None:
                productID_element = self.driver.find_element(By.XPATH, self.parameter_product_id)
                productID_element.send_keys(Keys.CONTROL + "a")  # Select all the existing text
                productID_element.send_keys(Keys.DELETE)  # Delete the selected text
                productID_element.send_keys(productID)  # Enter the new value

            else:
                print("No ProductID parameter. Hence, proceeding to execute.")
                pass

            self.driver.find_element(By.XPATH, self.execute).click()
            time.sleep(4)
            status_code_element = self.driver.find_element(By.XPATH, self.response_status_code)
            return status_code_element.text

        except ValueError:
            print(ValueError)

