import time

class LoginPage:
    USERNAMEINPUT = "//input[@id='login_username']"
    btnContinueLogin = "//button[@id='login_password_continue']"
    PASSWORDINPUT = "//input[@id='login_password']"
    btnLogin = "//button[@id='login_control_continue']"
    btnCloseCookie = "//button[@aria-label='Close']"
    username = ''
    password = ''
    btnPagination = "//button[contains(@class,'up-pagination-item up-btn' )]//span[contains(text(),'Next')]"
    
    
    def __init__(self,driver,username,password):
        self.driver = driver
        self.username = username
        self.password = password
    
    def enter_username(self):
        time
        self.driver.find_element("xpath",self.USERNAMEINPUT).send_keys(self.username)
        self.driver.find_element("xpath",self.btnContinueLogin).click()
    
    def enter_password(self):
        self.driver.find_element("xpath",self.PASSWORDINPUT).send_keys(self.password)
        self.driver.find_element("xpath",self.btnLogin).click()
    
    def login(self):
        
        # print(self.driver.page_source)
        self.enter_username()
        time.sleep(2)
        self.enter_password()
        time.sleep(5)

    def goToNextPage(self):
        self.driver.find_element("xpath",self.btnPagination).click()
