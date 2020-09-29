from github2 import username,password
from selenium import webdriver
import time
path="./msedgedriver.exe"
driver=webdriver.Edge(executable_path=path)
url="https://www.linkedin.com"
class Github:
    def __init__(self,username,password):
        self.browser=webdriver.Edge()
        self.username=username
        self.password=password

    def signIn(self):
        self.browser.get(url)

        time.sleep(2)

        self.browser.find_element_by_xpath("//*[@id='email']").send_keys(self.username)
        self.browser.find_element_by_xpath("//*[@id='pass']").send_keys(self.password)
        time.sleep(1)
        self.browser.find_element_by_xpath("//*[@id='loginbutton']").click()
github=Github(username,password)
github.signIn()
