from selenium import webdriver
import time
path="./msedgedriver.exe"
driver=webdriver.Edge(executable_path=path)
url="https://www.linkedin.com"
driver.get(url)
time.sleep(5)
driver.maximize_window()
url="https://www.linkedin.com/in/burak-yusuf-karabiyik-76b62b154/"
driver.get(url)
driver.save_screenshot("linkedin.com-homepage.png")
print(driver.title)
time.sleep(0)
driver.close()

