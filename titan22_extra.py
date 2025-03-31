from datetime import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

def get_driver(webpage):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("disable-infobars") #tar bort infomeddeladende
    chrome_options.add_argument("start-maximized") #största storlek
    chrome_options.add_argument("disable-dev-shm-usage") #Linus option.
    chrome_options.add_argument("no-sandbox")
    chrome_options.add_argument("disable-blink-features=AutomationControlled")
    chrome_options.add_experimental_option("detach", True)
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(webpage)
    return driver


driver = get_driver("https://titan22.com/account/login?return_url=%2Faccount")
loginname = driver.find_element(By.ID, "CustomerEmail")
password = driver.find_element(By.ID, "CustomerPassword")

loginname.send_keys("olov.sigurdson@gmail.com")
password.send_keys("Rap101010Clan" + Keys.ENTER)
time.sleep(1)

captcha = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/div/div/div[1]")


#driver.quit()