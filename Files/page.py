from locator import *
from sourcefiles import *
from element import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import imaplib
import imapclient
import email
import re
from bs4 import BeautifulSoup
import time
from urllib.parse import urlparse

# Each page deine inside class
# All selenium testing logics goes here


# All page classes inherit this
class BasePage(object):

    def __init__(self, driver):
        self.driver = driver
        self.elements = LoginPageElement(self.driver)
        self.elements_signout = SignOutPageElement(self.driver)
        self.elements_signup = SignUpPageElement(self.driver)
        self.elements_publish = PublishedPageElement(self.driver)
        self.elements_subcribe = SubcriptionPageElement(self.driver)


class LoginPage(BasePage):

    def is_portal_title_matches(self):
        return "Developer Portal" in self.driver.title

    def connect_server(self, serverName, myPort):

        try:
            self.elements.enter_server_name(serverName)
            self.elements.enter_port_number(myPort)
            self.elements.click_connect_button()

        except ValueError:
            print("Not working at all")
            print(ValueError)

    def enter_credentials(self, username, password):

        try:
            self.elements.enter_username(username)
            self.elements.enter_password(password)
            self.elements.click_login_button()

            # time.sleep(10)
            # self.driver.back()
            # time.sleep(5)

            print(self.driver.current_url)

        except ValueError:
            print(ValueError)

    # Send credentials using a file. Here a csv file

    def enter_credentials_via_file(self, filepath):

        # Read the CSV file and extract the rows
        with open(filepath, "r") as file:
            self.reader = csv.reader(file, delimiter=",")
            header = next(self.reader)
            self.rows = list(self.reader)

        # Loop through the rows and extract the values
        for row in self.rows:
            self.username_csv = row[0]
            self.password_csv = row[1]
            self.remember_me_csv = row[2]

            try:
                self.elements.enter_username(self.username_csv)
                self.elements.enter_password(self.password_csv)
                self.elements.click_login_button()

                print(self.driver.current_url)


                #Log in using the csv values failed
                if (self.driver.current_url != "http://localhost:9362/login" or "http://localhost:9362/"):

                    # Log in using the csv values passed
                    # time.sleep(10)
                    # self.driver.back()
                    # time.sleep(5)

                    assert self.driver.current_url == "http://localhost:9362/home"
                    print("Login successful with username: " + self.username_csv)
                    time.sleep(5)

                    # Now sign out
                    self.elements_signout.click_signout_button()
                    self.connect_server("HTTPS://LOCALHOST", "9262")

                    continue


                else:

                    assert self.driver.current_url == "http://localhost:9362/" or "http://localhost:9362/login"
                    print("Login failed with username: " + self.username_csv)
                    # self.fail("Login failed with username: " + username)
                    continue


            except ValueError:
                print(ValueError)


class SignUpPage(LoginPage):

    def set_up(self, serverName, myPort):
        LoginPage(self.driver).connect_server(serverName, myPort)

    def signup_page(self):
        self.elements_signup.click_signup_button()

    def is_portal_signup_title_matches(self):
        return self.elements_signup.signup_title_return()

    def user_registered_success(self):
        return self.elements_signup.signup_registered_notify()


    def enter_user_register_data(self, name, lastname, middlename, username, emailaddress, password, confirmpassword):

        try:
            self.elements_signup.enter_name(name)
            self.elements_signup.enter_lastname(lastname)
            self.elements_signup.enter_middlename(middlename)
            self.elements_signup.enter_username(username)
            self.elements_signup.enter_email_address(emailaddress)
            self.elements_signup.enter_password(password)
            self.elements_signup.enter_confirm_password(confirmpassword)
            self.elements_signup.click_register_button()
            time.sleep(20)

            assert self.driver.current_url == "http://localhost:9362/login"


        except ValueError:
            print(ValueError)

    def enter_signup_data_via_file(self, filepath):

        # Read the CSV file and extract the rows
        with open(filepath, "r") as file:
            self.reader = csv.reader(file, delimiter=",")
            header = next(self.reader)
            self.rows = list(self.reader)

        # Loop through the rows and extract the values
        for row in self.rows:
            username_csv = row[0]
            name_csv = row[1]
            middlename_csv = row[2]
            lastname_csv = row[3]
            emailaddress_csv = row[4]
            password_csv = row[5]
            confirmpassword_csv = row[6]

            try:
                self.elements_signup.enter_name(name_csv)
                self.elements_signup.enter_lastname(lastname_csv)
                self.elements_signup.enter_middlename(middlename_csv)
                self.elements_signup.enter_username(username_csv)
                self.elements_signup.enter_email_address(emailaddress_csv)
                self.elements_signup.enter_password(password_csv)
                self.elements_signup.enter_confirm_password(confirmpassword_csv)
                self.elements_signup.click_register_button()

                time.sleep(6)

                if self.driver.current_url == "http://localhost:9362/signup" :
                    assert self.driver.current_url == "http://localhost:9362/signup"
                    print("SignUp unsuccessful with username: " + username_csv)
                    continue

                else:
                    assert self.user_registered_success() != "User Registered!"
                    print("SignUp successful with username: " + username_csv + " and "+ name_csv)
                    self.signup_page()
                    continue

            except ValueError:
                print(ValueError)


    def verification_signup_email(self, imap_server, username, password, searching_criteria):

        # Set up the IMAP client
        # imap_server = imap_server # IMAP server for Hotmail/Outlook
        # self.username = username # Replace with your Hotmail/Outlook email address
        # self.password = password # Replace with your email password
        # self.search_criteria = searching_criteria
        #
        self.verification = False
        self.connect = input("Would you like to continue to connect to the mail y/n? ")

        if self.connect == ("n" or "no" or "No"):

            # Log out and close the connection
            #self.imap = imapclient.IMAPClient(imap_server , ssl=True)
            # or imap = imaplib.IMAP4_SSL(imap_server)
            #self.imap.logout()
            print("Terminating the connection")

        else:

            # Connect to the IMAP server
            #self.imap = imapclient.IMAPClient(imap_server , ssl=True)
            self.imap = imaplib.IMAP4_SSL(imap_server)

            # Log in to the email account
            self.imap.login(username, password)

            # Select the mailbox/folder you want to access (e.g., INBOX)
            self. imap.select_folder('INBOX')

            # Search for the latest emails i.e., 'SUBJECT "Astera Email Confirmation Link"'
            self.status, self.response = self.imap.search(None, searching_criteria)
            self.lastest_email_id = self.response[0].split()[-1]
            self.status, self.email_data = self.imap.fetch(self.latest_email_id, '(RFC822)')

            # Parse and process the email content using email.parser or other libraries
            self.raw_email = self.email_data[0][1]
            self.parsed_email = email.message_from_string(self.raw_email)

            # Process the email data as needed
            # You can use the BODY[] or RFC822 section specifier in the fetch() method.
            # self.raw_email = self.email_data[msg_id][b'BODY[]'].decode('utf-8')

            # Extract links from the message body or HTML parts
            if self.parsed_email.is_multipart():
                for part in self.parsed_email.walk():
                    self.content_type = part.get_content_type()
                    if self.content_type == 'text/plain':
                        self.email_text = part.get_payload(decode=True).decode('utf-8')
                        print(self.email_text)
                        break
            else:
                self.email_text = self.parsed_email.get_payload(decode=True).decode('utf-8')
                print(self.email_text)


        # Now Extract links using regular expressions


            try:
                # Open the link in a browser
                link = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', self.email_text)
                self.driver.get(link)

                # Select the back to log in button
                # Write the code here then
                assert self.driver.current_url == "http://localhost:9362/login"

                self.imap.close()
                self.imap.logout()
                self.verification = True


            except(ValueError):

                print("Verification failed")

        print(self.verification)
        return self.verification




    def verify_validate_signup(self, username, password):

        # add code for verification # review this line
        if self.verification != True:
            print("The user with username: "+ username +"  is not verified yet. \n"
                                           "Please use the link sent to your email address for verification and try again." )

        else:
            assert self.verification
            print("The user has successfully verified the email.")

            LoginPage.enter_credentials(username, password)

            if (self.driver.current_url == "http://localhost:9362/home"):

                assert self.driver.current_url == "http://localhost:9362/home"

                print("Login successful with username: " + username)
                # Now sign out
                self.elements_signout.click_signout_button()

            else:
                assert self.driver.current_url == "http://localhost:9362/home"
                print("Login failed with username: " + username)


  #Need to fix this, the error messages are not being captured
    def verify_signup_fields(self, name, lastname, middlename, username, emailaddress, password, confirmpassword):

        try:
            #Enter value to the fields
            self.elements_signup.enter_name(name)
            self.elements_signup.enter_lastname(lastname)
            self.elements_signup.enter_middlename(middlename)
            self.elements_signup.enter_username(username)
            self.elements_signup.enter_email_address(emailaddress)
            self.elements_signup.enter_password(password)
            self.elements_signup.enter_confirm_password(confirmpassword)

            #Press register button
            #self.elements_signout.click_signout_button()

            # Capture all the text messages under the fields
            elements_captured = self.elements_signup.capture_name_text()
            print(elements_captured)

            if elements_captured is None:
                assert True
                print("Field verification passsed!")

            else:

                captured_texts = []

                # Capture the text of each element
                for x in elements_captured:
                    captured_texts.append(x.text)

                # Iterate through the captured texts
                for text in captured_texts:
                    print(text)
                    print("\n")

                assert False

        except ValueError:
            print(ValueError)



class PublishedPage(LoginPage):

    def publish_page_button(self):
        self.elements_publish.click_publishdpage_button()


    def publish_page_heading(self):
        return self.elements_publish.heading_publishedpage()


    def click_on_subscribe_button(self):
        self.elements_publish.subscribe_expand_publishedpage()
        self.elements_publish.subscribe_button_publishedpage()

    def notification_of_subscribe_request(self):
        return self.elements_publish.successful_request_notification()


class SubscriptionPage(LoginPage):

    def subscribe_page_button(self):

        try:
            self.elements_subcribe.click_subscribepage_button()
        except ValueError:
            print(ValueError)


    def click_on_swagger_button(self):
        self.elements_subcribe.subscribe_expand_subscribepage()
        self.elements_subcribe.swagger_button_subscribepage()


    def title_of_swagger_ui(self):
        return self.elements_subcribe.title_swagger()


    def return_open_swagger_URL(self):

        try:
            self.url = self.elements_subcribe.URL_swagger()
            # open swagger url
            self.driver.get(self.url)
            time.sleep(3)

            assert self.url == self.driver.current_url

        except ValueError:
            print(ValueError)


        # swagger_url = urlparse(self.elements_subcribe.URL_swagger())
        # browser_url = urlparse(self.driver.current_url).geturl()
        #
        # assert swagger_url == browser_url

        # self.elements_subcribe.URL_swagger() == repr(self.driver.current_url)


    def perform_endpoint_call(self, bearerToken, productID):

        try:
            self.elements_subcribe.authorize_button()
            self.elements_subcribe.auth_textbox(bearerToken)
            self.elements_subcribe.token_auth_button()
            self.elements_subcribe.auth_close_button()
            self.elements_subcribe.expand_endpoint()
            self.elements_subcribe.try_it_out_button()

            if productID is not None:
                self.elements_subcribe.parameter_product_id(productID)

            else:
                print("No ProductID parameter. Hence, proceeding to execute.")
                pass

            self.elements_subcribe.execute()
            return self.elements_subcribe.response_status_code()

        except ValueError:
            print(ValueError)












