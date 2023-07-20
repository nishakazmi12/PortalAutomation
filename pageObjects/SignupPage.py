from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import imaplib
import imapclient
import email
import re
import time


class SignupPage:

    # Locators for Login
    enter_port_number = "Port"
    enter_server_name = "Host"
    click_connect_button = "button[class*='serverconnection_connect-btn']"

    enter_login_username = "User"
    enter_login_password = "Password"
    click_login_button = "//body/div[@id='root']/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[4]/div[1]/div[1]/div[1]/div[1]/button[1]"


    # Locator for Sign out
    button_sighOut_xpath = "//body/div[@id='root']/section[1]/section[1]/aside[1]/div[1]/ul[1]/li[4]"


    # Locators for Sign up Page
    click_button_signup = "//body/div[@id='root']/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[4]/div[1]/div[1]/div[1]/div[1]/button[2]"
    signup_title_return = "h5"
    enter_name = "FirstName"
    enter_lastname = "LastName"
    enter_middlename = "MiddleName"
    enter_username = "UserName"
    enter_email_address = "Email"
    enter_password = "Password"
    enter_confirm_password = "ConfirmPassword"
    click_register_button = "//body/div[@id='root']/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/form[1]/div[6]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/button[1]"
    capture_name_text = "ant-form-item-explain-error"
    signup_registered_notify = "ant-notification-notice-message"
    success_registered = (By.XPATH, "//div[contains(text(),'User Registered!')]")


    def __init__(self, driver):
        self.success_registered_element = None
        self.email_text = None
        self.verification = None
        self.driver = driver

    # def set_up(self, serverName, myPort):
    #
    #     try:
    #         enter_port_number_element = self.driver.find_element(By.ID, self.enter_port_number)
    #         enter_port_number_element.send_keys(Keys.CONTROL + "a")
    #         enter_port_number_element.send_keys(Keys.DELETE)
    #         enter_port_number_element.send_keys(myPort)
    #
    #         enter_server_name_element = self.driver.find_element(By.ID, self.enter_server_name)
    #         enter_server_name_element.send_keys(Keys.CONTROL + "a")
    #         enter_server_name_element.send_keys(Keys.DELETE)
    #         enter_server_name_element.send_keys(serverName)
    #
    #         self.driver.find_element(By.CSS_SELECTOR, self.click_connect_button)
    #
    #     except ValueError:
    #         print("Not working at all")
    #         print(ValueError)

    def enter_credentials(self, username, password):

        try:
            enter_username_element = self.driver.find_element(By.ID, self.enter_login_username)
            enter_username_element.send_keys(Keys.CONTROL + "a")
            enter_username_element.send_keys(Keys.DELETE)
            enter_username_element.send_keys(username)

            enter_password_element = self.driver.find_element(By.ID, self.enter_login_password)
            enter_password_element.send_keys(Keys.CONTROL + "a")
            enter_password_element.send_keys(Keys.DELETE)
            enter_password_element.send_keys(password)

            click_login_button_element = self.driver.find_element(By.XPATH, self.click_login_button)
            click_login_button_element.click()

        except ValueError:
            print(ValueError)


    def signup_page_button(self):
        click_button_signup_element = self.driver.find_element(By.XPATH, self.click_button_signup)
        click_button_signup_element.click()


    def is_portal_signup_title_matches(self):
        return self.driver.find_element(By.TAG_NAME, self.signup_title_return).text

    def user_registered_success(self):
        return self.driver.find_element(By.CLASS_NAME, self.signup_registered_notify)

    def enter_user_register_data(self, name, lastname, middlename, username, emailaddress, password, confirmpassword):

        try:
            enter_name_element = self.driver.find_element(By.ID, self.enter_name)
            enter_name_element.send_keys(Keys.CONTROL + "a")
            enter_name_element.send_keys(Keys.DELETE)
            enter_name_element.send_keys(name)

            enter_lastname_element = self.driver.find_element(By.ID, self.enter_lastname)
            enter_lastname_element.send_keys(Keys.CONTROL + "a")
            enter_lastname_element.send_keys(Keys.DELETE)
            enter_lastname_element.send_keys(lastname)

            enter_middlename_element = self.driver.find_element(By.ID, self.enter_middlename)
            enter_middlename_element.send_keys(Keys.CONTROL + "a")
            enter_middlename_element.send_keys(Keys.DELETE)
            enter_middlename_element.send_keys(middlename)

            enter_username_element = self.driver.find_element(By.ID, self.enter_username)
            enter_username_element.send_keys(Keys.CONTROL + "a")
            enter_username_element.send_keys(Keys.DELETE)
            enter_username_element.send_keys(username)

            enter_emailaddress_element = self.driver.find_element(By.ID, self.enter_email_address)
            enter_emailaddress_element.send_keys(Keys.CONTROL + "a")
            enter_emailaddress_element.send_keys(Keys.DELETE)
            enter_emailaddress_element.send_keys(emailaddress)

            enter_password_element = self.driver.find_element(By.ID, self.enter_password)
            enter_password_element.send_keys(Keys.CONTROL + "a")
            enter_password_element.send_keys(Keys.DELETE)
            enter_password_element.send_keys(password)

            enter_confirmpassword_element = self.driver.find_element(By.ID, self.enter_confirm_password)
            enter_confirmpassword_element.send_keys(Keys.CONTROL + "a")
            enter_confirmpassword_element.send_keys(Keys.DELETE)
            enter_confirmpassword_element.send_keys(confirmpassword)

            self.driver.find_element(By.XPATH, self.click_register_button).click()

            success_registered_element = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(self.success_registered)
            )

            assert success_registered_element.text == "User Registered!"

            #OR
            # assert self.driver.current_url == "http://localhost:3000/login"


        except ValueError:
            print(ValueError)

    def enter_signup_data_via_file(self, filepath):

        # Read the CSV file and extract the rows
        with open(filepath, "r") as file:
            reader = csv.reader(file, delimiter=",")
            header = next(reader)
            rows = list(reader)

        # Loop through the rows and extract the values
        for row in rows:
            username_csv = row[0]
            name_csv = row[1]
            middlename_csv = row[2]
            lastname_csv = row[3]
            emailaddress_csv = row[4]
            password_csv = row[5]
            confirmpassword_csv = row[6]

            try:
                enter_name_element = self.driver.find_element(By.ID, self.enter_name)
                enter_name_element.send_keys(Keys.CONTROL + "a")
                enter_name_element.send_keys(Keys.DELETE)
                enter_name_element.send_keys(name_csv)

                enter_lastname_element = self.driver.find_element(By.ID, self.enter_lastname)
                enter_lastname_element.send_keys(Keys.CONTROL + "a")
                enter_lastname_element.send_keys(Keys.DELETE)
                enter_lastname_element.send_keys(lastname_csv)

                enter_middlename_element = self.driver.find_element(By.ID, self.enter_middlename)
                enter_middlename_element.send_keys(Keys.CONTROL + "a")
                enter_middlename_element.send_keys(Keys.DELETE)
                enter_middlename_element.send_keys(middlename_csv)

                enter_username_element = self.driver.find_element(By.ID, self.enter_username)
                enter_username_element.send_keys(Keys.CONTROL + "a")
                enter_username_element.send_keys(Keys.DELETE)
                enter_username_element.send_keys(username_csv)

                enter_emailaddress_element = self.driver.find_element(By.ID, self.enter_email_address)
                enter_emailaddress_element.send_keys(Keys.CONTROL + "a")
                enter_emailaddress_element.send_keys(Keys.DELETE)
                enter_emailaddress_element.send_keys(emailaddress_csv)

                enter_password_element = self.driver.find_element(By.ID, self.enter_password)
                enter_password_element.send_keys(Keys.CONTROL + "a")
                enter_password_element.send_keys(Keys.DELETE)
                enter_password_element.send_keys(password_csv)

                enter_confirmpassword_element = self.driver.find_element(By.ID, self.enter_confirm_password)
                enter_confirmpassword_element.send_keys(Keys.CONTROL + "a")
                enter_confirmpassword_element.send_keys(Keys.DELETE)
                enter_confirmpassword_element.send_keys(confirmpassword_csv)

                self.driver.find_element(By.XPATH, self.click_register_button).click()

                time.sleep(6)

                # self.success_registered_element = WebDriverWait(self.driver, 20).until(
                #     EC.visibility_of_element_located(self.success_registered)
                # )
                #
                # if self.success_registered_element.text == "User Registered!":
                #     assert True
                #     print("SignUp successful with username: " + username_csv)
                #     self.signup_page_button()
                #     continue
                #
                # else:
                #     print("SignUp unsuccessful with username: " + username_csv + " and " + name_csv)
                #     continue

                if self.driver.current_url == "http://localhost:3000/login":
                    assert True
                    print("SignUp successful with username: " + username_csv)
                    self.signup_page_button()
                    continue

                else:
                    print("SignUp unsuccessful with username: " + username_csv + " and " + name_csv)
                    continue


            except ValueError:
                print(ValueError)

    def verification_signup_email(self, imap_server, port_number, username, password, searching_criteria):

        # Set up the IMAP client
        # imap_server = imap_server # IMAP server for Hotmail/Outlook
        # self.username = username # Replace with your Hotmail/Outlook email address
        # self.password = password # Replace with your email password
        # self.search_criteria = searching_criteria

        self.verification = False
        connect = input("Would you like to continue to connect to the mail y/n? ")

        if connect == ("n" or "no" or "No"):

            # Log out and close the connection
            # self.imap = imapclient.IMAPClient(imap_server , ssl=True)
            # or imap = imaplib.IMAP4_SSL(imap_server)
            # self.imap.logout()
            print("Terminating the connection")

        else:

            # Connect to the IMAP server
            imap = imapclient.IMAPClient(imap_server, port_number, ssl=True)
            print(username)
            print(password)
            #imap = imaplib.IMAP4_SSL(imap_server)

            # Log in to the email account
            imap.login(username, password)

            # Select the mailbox/folder you want to access (e.g., INBOX)
            imap.select_folder('INBOX')

            # Search for the latest emails i.e., 'SUBJECT "Astera Email Confirmation Link"'
            status, response = imap.search(None, searching_criteria)
            latest_email_id = response[0].split()[-1]
            status, email_data = imap.fetch(latest_email_id, '(RFC822)')

            # Parse and process the email content using email.parser or other libraries
            raw_email = email_data[0][1]
            parsed_email = email.message_from_string(raw_email)

            # Process the email data as needed
            # You can use the BODY[] or RFC822 section specifier in the fetch() method.
            # self.raw_email = self.email_data[msg_id][b'BODY[]'].decode('utf-8')

            # Extract links from the message body or HTML parts
            if parsed_email.is_multipart():
                for part in parsed_email.walk():
                    content_type = part.get_content_type()
                    if content_type == 'text/plain':
                        self.email_text = part.get_payload(decode=True).decode('utf-8')
                        print(self.email_text)
                        break
            else:
                self.email_text = parsed_email.get_payload(decode=True).decode('utf-8')
                print(self.email_text)

            # Now Extract links using regular expressions

            try:
                # Open the link in a browser
                link = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', self.email_text)
                self.driver.get(link)

                # Select the back to log in button
                # Write the code here then
                assert self.driver.current_url == "http://localhost:3000/login"

                imap.logout()
                self.verification = True


            except ValueError:

                print("Verification failed")

        print(self.verification)
        return self.verification

    def verify_validate_signup(self, verficationBoolean, username, password):

        # add code for verification # review this line
        if verficationBoolean:
            print("The user with username: " + username + "  is not verified yet. \n"
                                                          "Please use the link sent to your email address for verification and try again.")

        else:
            print("The user has successfully verified the email.")
            self.enter_credentials(username, password)

            if self.driver.current_url == "http://localhost:3000/home":
                assert True
                print("Login successful with username: " + username)
                self.driver.find_element(By.XPATH, self.button_sighOut_xpath).click()

            else:
                print("Login failed with username: " + username)
                assert False


    def verify_signup_fields(self, name, lastname, middlename, username, emailaddress, password, confirmpassword):

        try:
            # Enter value to the fields
            enter_name_element = self.driver.find_element(By.ID, self.enter_name)
            enter_name_element.send_keys(Keys.CONTROL + "a")
            enter_name_element.send_keys(Keys.DELETE)
            enter_name_element.send_keys(name)

            enter_lastname_element = self.driver.find_element(By.ID, self.enter_lastname)
            enter_lastname_element.send_keys(Keys.CONTROL + "a")
            enter_lastname_element.send_keys(Keys.DELETE)
            enter_lastname_element.send_keys(lastname)

            enter_middlename_element = self.driver.find_element(By.ID, self.enter_middlename)
            enter_middlename_element.send_keys(Keys.CONTROL + "a")
            enter_middlename_element.send_keys(Keys.DELETE)
            enter_middlename_element.send_keys(middlename)

            enter_username_element = self.driver.find_element(By.ID, self.enter_username)
            enter_username_element.send_keys(Keys.CONTROL + "a")
            enter_username_element.send_keys(Keys.DELETE)
            enter_username_element.send_keys(username)

            enter_emailaddress_element = self.driver.find_element(By.ID, self.enter_email_address)
            enter_emailaddress_element.send_keys(Keys.CONTROL + "a")
            enter_emailaddress_element.send_keys(Keys.DELETE)
            enter_emailaddress_element.send_keys(emailaddress)

            enter_password_element = self.driver.find_element(By.ID, self.enter_password)
            enter_password_element.send_keys(Keys.CONTROL + "a")
            enter_password_element.send_keys(Keys.DELETE)
            enter_password_element.send_keys(password)

            enter_confirmpassword_element = self.driver.find_element(By.ID, self.enter_confirm_password)
            enter_confirmpassword_element.send_keys(Keys.CONTROL + "a")
            enter_confirmpassword_element.send_keys(Keys.DELETE)
            enter_confirmpassword_element.send_keys(confirmpassword)


            # Capture all the text messages under the fields
            elements_captured = self.driver.find_element(By.CLASS_NAME, self.capture_name_text).text

            if elements_captured is None:
                print("Field verification passsed!")

            else:
                # captured_texts = []
                #
                # # Capture the text of each element
                # for x in elements_captured:
                #     captured_texts.append(x.text)
                #
                # # Iterate through the captured texts
                # for text in captured_texts:
                #     print(text)
                #     print("\n")
                # Iterate through the captured texts
                print(elements_captured)
                assert True


        except ValueError:
            print(ValueError)
