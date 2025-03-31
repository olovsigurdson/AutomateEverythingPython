from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import yagmail
sender = "olov.sigurdson@gmail.com"
receiver = "olov.sigurdson@tietoevry.com"


def get_driver(webpage):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("disable-infobars")  # tar bort infomeddeladende
    chrome_options.add_argument("start-maximized")  # största storlek
    chrome_options.add_argument("disable-dev-shm-usage")  # Linus option.
    chrome_options.add_argument("no-sandbox")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("disable-blink-features=AutomationControlled")
    chrome_options.add_experimental_option("detach", True)
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(webpage)
    return driver


def clean_test(input_text):
    return float(input_text[:-2])

driver = get_driver("https://zse.hr/en/indeks-366/365?isin=HRZB00ICBEX6")
# firstname = driver.find_element(By.XPATH, "/html/body/div[1]/div/h1[1]")
time.sleep(5)
stock_exchange = driver.find_element(By.XPATH, "//span[contains(@class, 'stock-trend trend-drop')]")
stock_exchange_res = clean_test(stock_exchange.text)

if stock_exchange_res < -0.10:
    subject = f"Nu är börsen nere på {stock_exchange_res}%"
    content = """
    Det finns saker att göra!
    """
    yag = yagmail.SMTP(user=sender, password="cuayewzipxmbnvfq")
    yag.send(to=receiver, subject=subject, contents=content)
else:
    print(f"Lugnt! börsen ligger på {stock_exchange_res}")
