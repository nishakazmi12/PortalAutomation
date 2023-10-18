import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from locator import *



class BaseElement(object):
    def __init__(self,driver):
        self.driver = driver

    # Use this macro before sending key value in any textbox
    # def clear_textbox(self):
    #     element.send_keys(Keys.CONTROL + "a")
    #     element.send_keys(Keys.DELETE)


#To Do-> make this class genarlized add getter and setter 
class LoginPageElement(BaseElement):

    def enter_server_name(self, serverName):

        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(LoginPageLocators.Server_Name_Box)
        )
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.DELETE)
        element.send_keys(serverName)

    def enter_port_number(self, port):

        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(LoginPageLocators.Port_Text_Box)
        )
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.DELETE)
        element.send_keys(port)

    def click_connect_button(self):

        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(LoginPageLocators.Connect_Button)
        )
        ActionChains(self.driver).move_to_element(element).click().perform()
    
    def enter_username(self, username):

        element = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(LoginPageLocators.Username)
        )
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.DELETE)
        element.send_keys(username)
    
    def enter_password(self, password):

        element = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(LoginPageLocators.Password)
        )
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.DELETE)
        element.send_keys(password)

    def click_login_button(self):

        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(LoginPageLocators.Login)
        )
        ActionChains(self.driver).move_to_element(element).click().perform()
    

class SignOutPageElement(BaseElement):

    def click_signout_button(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(SignOutPageLocators.Sign_Out_Button)
        )
        ActionChains(self.driver).move_to_element(element).click().perform()


class SignUpPageElement(BaseElement):

    def click_signup_button(self):
        element = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(SignUpPageLocators.Sign_Up_Button)
        )
        ActionChains(self.driver).move_to_element(element).click().perform()

    def signup_title_return(self):
        element = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(SignUpPageLocators.SignUp_Title)
        )
        return element.text

    def enter_name(self, name):

        element = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(SignUpPageLocators.Name)
        )
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.DELETE)
        element.send_keys(name)

    def enter_lastname(self, lastname):

        element = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(SignUpPageLocators.LastName)
        )
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.DELETE)
        element.send_keys(lastname)

    def enter_middlename(self, middlename):
        element = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(SignUpPageLocators.MiddleName)
        )
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.DELETE)
        element.send_keys(middlename)

    def enter_username(self, username):

        element = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(SignUpPageLocators.UserName)
        )
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.DELETE)
        element.send_keys(username)

    def enter_email_address(self, emailaddress):
        element = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(SignUpPageLocators.Email_Address)
        )
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.DELETE)
        element.send_keys(emailaddress)

    def enter_password(self, password):

        element = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(SignUpPageLocators.Password)
        )
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.DELETE)
        element.send_keys(password)

    def enter_confirm_password(self, confirmpassword):

        element = WebDriverWait(self.driver,20).until(
            EC.presence_of_element_located(SignUpPageLocators.Confirm_Password)
        )
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.DELETE)
        element.send_keys(confirmpassword)

    def click_register_button(self):

        element = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(SignUpPageLocators.Register_Button)
        )
        ActionChains(self.driver).move_to_element(element).click().perform()


    def capture_name_text(self):
        element = WebDriverWait(self.driver, 100).until(
            EC.presence_of_all_elements_located(SignUpPageLocators.CaptureText_SignUp)
        )
        return element

    def signup_registered_notify(self):
        element = WebDriverWait(self.driver, 100).until(
            EC.visibility_of_element_located(SignUpPageLocators.UserRegistered)
        )
        return element.text



class PublishedPageElement(BaseElement):

    def click_publishdpage_button(self):
        element = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(PublishedPageLocators.PublishListItem)
        )
        ActionChains(self.driver).move_to_element(element).click().perform()


    def heading_publishedpage(self):
        element = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(PublishedPageLocators.PublishHeading)
        )
        return element.text


    def subscribe_expand_publishedpage(self):
        element = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(PublishedPageLocators.ProductExpand)
        )
        ActionChains(self.driver).move_to_element(element).click().perform()


    def subscribe_button_publishedpage(self):
        element = WebDriverWait(self.driver, 50).until(
            EC.element_to_be_clickable(PublishedPageLocators.SubscribeButton)
        )
        ActionChains(self.driver).move_to_element(element).click().perform()


    def successful_request_notification(self):
        element = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(PublishedPageLocators.SubscribeNotify)
        )
        return element.text


class SubcriptionPageElement(BaseElement):


    def click_subscribepage_button(self):
        element = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(SubscriptionPageLocators.SubscribeListItem)
        )
        ActionChains(self.driver).move_to_element(element).click().perform()

    def subscribe_expand_subscribepage(self):
        element = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(SubscriptionPageLocators.SubscriptionExpand)
        )
        ActionChains(self.driver).move_to_element(element).click().perform()


    def swagger_button_subscribepage(self):
        element = WebDriverWait(self.driver, 50).until(
            EC.element_to_be_clickable(SubscriptionPageLocators.Swagger_UI)
        )
        ActionChains(self.driver).move_to_element(element).click().perform()

    def title_swagger(self):
        element = WebDriverWait(self.driver, 50).until(
            EC.visibility_of_element_located(SubscriptionPageLocators.Swagger_Title)
        )
        return element.text

    def URL_swagger(self):
        element = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(SubscriptionPageLocators.Swagger_URL)
        )
        return element.get_attribute('href')

    def authorize_button(self):
        element = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(SubscriptionPageLocators.Authorize_Button)
            )
        ActionChains(self.driver).move_to_element(element).click().perform()

    def auth_textbox(self, bearerToken):
        element = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(SubscriptionPageLocators.Token_TextBox)
            )
        ActionChains(self.driver).move_to_element(element).click().send_keys_to_element(element, bearerToken).perform()

    def token_auth_button(self):
        element = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(SubscriptionPageLocators.Auth_Token_Button)
        )
        ActionChains(self.driver).move_to_element(element).click().perform()

    def auth_close_button(self):
        element = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(SubscriptionPageLocators.Auth_Close_Button)
        )
        ActionChains(self.driver).move_to_element(element).click().perform()

    def expand_endpoint(self):
        element = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(SubscriptionPageLocators.Expand_Endpoint)
        )
        time.sleep(2)
        ActionChains(self.driver).move_to_element(element).click().perform()

    def try_it_out_button(self):
        element = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(SubscriptionPageLocators.Try_It_Out_Button)
        )
        ActionChains(self.driver).move_to_element(element).click().perform()

    def parameter_product_id(self, productID):
        element = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(SubscriptionPageLocators.Product_ID)
            )
        ActionChains(self.driver).move_to_element(element).click().send_keys_to_element(element, productID).perform()

    def execute(self):
        element = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(SubscriptionPageLocators.Execute_Button)
            )
        ActionChains(self.driver).move_to_element(element).click().perform()

    def response_status_code(self):
        element = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(SubscriptionPageLocators.Response_Code)
            )
        return element.text


