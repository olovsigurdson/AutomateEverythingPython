from selenium import webdriver

chrome_options= webdriver.ChromeOptions()
chrome_options.add_argument("disable-infobars")
chrome_options.add_argument("start-maximized")
chrome_options.add_argument("disable-dev-shm-usage")
chrome_options.add_argument("no-sandbox")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])

driver = webdriver.Chrome(options=chrome_options)


print(-0.4 < -0.11)