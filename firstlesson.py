from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import re
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

def clean_test(input_text):
    return float(input_text[-2:])


driver = get_driver("https://automated.pythonanywhere.com")
#firstname = driver.find_element(By.XPATH, "/html/body/div[1]/div/h1[1]")
time.sleep(5)
weather = driver.find_element(By.XPATH, "/html/body/div[1]/div/h1[2]")
print(clean_test(weather.text))

# firstname.send_keys("Olov")
#
# lastname = driver.find_element(By.NAME, "lName")
# lastname.send_keys("Sigurdson")
#
# lastname = driver.find_element(By.NAME, "email")
# lastname.send_keys("olov.siugurweinb@gmail.com")
#
# button = driver.find_element(By.CLASS_NAME, "btn")
# button.click()
#driver.quit()