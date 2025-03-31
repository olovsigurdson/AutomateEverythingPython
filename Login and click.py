from datetime import datetime

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


driver = get_driver("https://automated.pythonanywhere.com/login/")
loginname = driver.find_element(By.ID, "id_username")
password = driver.find_element(By.ID, "id_password")

loginname.send_keys("automated")
time.sleep(1)
password.send_keys("automatedautomated" + Keys.ENTER)

time.sleep(2)
home = driver.find_element(By.CLASS_NAME, "navbar-brand")
home.click()

time.sleep(4)

times = 0

while times < 10:
    time.sleep(4)
    weather = driver.find_element(By.XPATH, "/html/body/div[1]/div/h1[2]")

    # Hämta nuvarande datum och tid
    now = datetime.now()

    # Formatera till 'YYYYMMDD HHSS'
    formatted_date_time = now.strftime('%Y%m%d %H%M %S')

    with open(f"temperature_{formatted_date_time}.txt", "w") as file_temp:
        temperature = clean_test(weather.text)
        file_temp.write(str(temperature))

    times += 1

driver.quit()

#print(clean_test(weather.text))

#Keys.ENTER funkar också
#login_click = driver.find_element(By.CLASS_NAME, "btn")
#login_click.click()

