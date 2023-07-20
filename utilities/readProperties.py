import configparser

config = configparser.RawConfigParser()
config.read(".\\Configuration\\config.ini")


class ReadConfig:

    @staticmethod
    def getApplicationURL():
        baseUrl = config.get('common info', 'baseUrl')
        return baseUrl

    @staticmethod
    def getUsername():
        username = config.get('common info', 'username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password

    @staticmethod
    def getPort():
        port = config.get('common info', 'port')
        return port

    @staticmethod
    def getUsernameSignup():
        username_signup = config.get('common info', 'username_signup')
        return username_signup

    @staticmethod
    def getFirstnameSignup():
        name_signup = config.get('common info', 'name_signup')
        return name_signup

    @staticmethod
    def getLastnameSignup():
        lastname_signup = config.get('common info', 'lastname_signup')
        return lastname_signup

    @staticmethod
    def getMiddlenameSignup():
        middlename_signup = config.get('common info', 'middlename_signup')
        return middlename_signup

    @staticmethod
    def getEmailSignup():
        email_signup = config.get('common info', 'emailaddress_signup')
        return email_signup

    @staticmethod
    def getPasswordSignup():
        password_signup = config.get('common info', 'password_signup')
        return password_signup

    @staticmethod
    def getConfirmPassword():
        confirmpassword_signup = config.get('common info', 'confirmpassword_signup')
        return confirmpassword_signup

    @staticmethod
    def getEmailEmailAdd():
        email_signup = config.get('common info', 'email_address')
        return email_signup

    @staticmethod
    def getEmailPassword():
        password_signup = config.get('common info', 'email_password')
        return password_signup

    @staticmethod
    def getEmailServer():
        email_server = config.get('common info', 'email_server')
        return email_server

    @staticmethod
    def getEmailSubject():
        email_subject = config.get('common info', 'email_subject')
        return email_subject

    @staticmethod
    def getEmailPort():
        email_port = config.get('common info', 'email_port')
        return email_port
