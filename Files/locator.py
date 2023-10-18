from selenium.webdriver.common.by import By


#All css id/class/name locator shoudl define in this file 
#Each class has it's own locator

class LoginPageLocators(object):
    Port_Text_Box= (By.ID, "Port")
    Connect_Button = (By.CSS_SELECTOR, "button[class*='serverconnection_connect-btn']")
    #Connect_Button=(By.CLASS_NAME,"ant-btn ant-btn-primary serverconnection_connect-btn__zYZhk")
    Login_Active=(By.CLASS_NAME, "ant-steps-item ant-steps-item-process ant-steps-item-active")
    Username=(By.ID, "User")
    Password=(By.ID,"Password")
    Login=(By.XPATH,"//body/div[@id='root']/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[4]/div[1]/div[1]/div[1]/div[1]/button[1]")
    #ant-btn ant-btn-primary login_connect-btn__8fRWV
    #class="ant-btn ant-btn-primary serverconnection_connect-btn__aoQ0K"
    Server_Name_Box = (By.ID, "Host")

class SignOutPageLocators(object):

    # Customized XPath Syntax
    # "//tagname[@attribute='value']"
    Sign_Out_Button = (By.XPATH, "//body/div[@id='root']/section[1]/section[1]/aside[1]/div[1]/ul[1]/li[4]")

class SignUpPageLocators(object):

    # Customized CSS Syntax
    # tagname[attributeName='attributeValue'] ---Tagname optional
    # input[name = 'search_query']

    Sign_Up_Button = (By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[4]/div[1]/div[1]/div[1]/div[1]/button[2]")
    SignUp_Title = (By.TAG_NAME, "h5")
    Name = (By.ID, "FirstName")
    LastName = (By.ID, "LastName")
    MiddleName = (By.ID, "MiddleName")
    UserName = (By.ID, "UserName")
    Email_Address = (By.ID, "Email")
    Password = (By.ID, "Password")
    Confirm_Password = (By.ID, "ConfirmPassword")
    #<button type="submit" class="ant-btn ant-btn-primary ant-btn-block signup_register-btn__DDZ8G" ><span>Register</span></button>
    Register_Button = (By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/form[1]/div[6]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/button[1]")
    #CaptureText_SignUp = (By.XPATH, "//div[@class='ant-form-item-explain-error']")
    CaptureText_SignUp = (By.CLASS_NAME, "ant-form-item-explain-error")
    #CaptureText_SignUp = (By.CSS_SELECTOR, "div.ant-form-item-explain-error")
    UserRegistered =(By.CLASS_NAME, "ant-notification-notice-message")
    #<div class="ant-notification-notice-message">User Registered!</div>
    #//body/div[2]/div[1]/div[1]/div[1]

class PublishedPageLocators(object):

    PublishListItem = (By.XPATH, "//body/div[@id='root']/section[1]/section[1]/aside[1]/div[1]/ul[1]/li[1]")
    PublishHeading = (By.XPATH, "//h1[contains(text(),'Welcome to Developer Portal')]")
    ProductExpand = (By.XPATH, "//body/div[@id='root']/section[1]/section[1]/main[1]/div[2]/div[1]/div[1]/div[1]/div[1]")
    SubscribeButton = (By.XPATH, "//body/div[@id='root']/section[1]/section[1]/main[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/button[1]")
    SubscribeNotify = (By.XPATH, "//div[@class='ant-notification-notice-message']")

class SubscriptionPageLocators(object):

    SubscribeListItem = (By.XPATH, "//body/div[@id='root']/section[1]/section[1]/aside[1]/div[1]/ul[1]/li[2]")
    SubscriptionExpand = (By.XPATH, "//body/div[@id='root']/section[1]/section[1]/main[1]/div[2]/div[1]/div[1]/div[1]/div[1]")
    Swagger_UI = (By.XPATH, "//body/div[@id='root']/section[1]/section[1]/main[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/button[1]")
    Swagger_Title = (By.XPATH, "//div[@id=':r0:']")
    Swagger_URL = (By.XPATH,  "//a[@class='link']")
    Authorize_Button = (By.XPATH, "//span[contains(text(),'Authorize')]")
    Token_TextBox = (By.XPATH, "//input[@aria-label='auth-bearer-value']")
    Auth_Token_Button = (By.XPATH, "//button[contains(text(),'Authorize')]")
    Auth_Close_Button = (By.XPATH, "//button[contains(text(),'Close')]")
    Auth_Logout_Button = (By.XPATH, "//button[contains(text(),'Logout')]")
    Expand_Endpoint = (By.XPATH, "//div[contains(text(),'[GET]Products1")
    Try_It_Out_Button = (By.XPATH, "//button[contains(text(),'Try it out')]")
    Product_ID = (By.XPATH, "//tbody/tr[1]/td[2]/input[1]")
    Execute_Button = (By.XPATH, "//button[contains(text(),'Execute')]")
    Response_Code = (By.XPATH, "//body[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[2]/div[4]/section[1]/div[1]/span[1]/div[1]/div[1]/div[1]/span[2]/div[1]/div[2]/div[1]/div[4]/div[2]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[1]")








