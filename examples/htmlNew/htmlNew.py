from selenium import webdriver
from selenium.webdriver.common.keys import keys
import time
path="./msedgedriver.exe"
driver=webdriver.Edge(executable_path=path)
url="http://github.com"
driver.get(url)
searchInput=driver.find_element_by_name("q")
time.sleep(1)
searchInput.send_keys("python")
time.sleep(2)
searchInput.send_keys(Keys.ENTER)
time sleep(2)
driver.close()


