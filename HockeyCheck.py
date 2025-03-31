from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initiera Chromedriver
driver = webdriver.Chrome()

# Navigera till webbsidan
url = 'https://skelleftea.se/invanare/startsida/uppleva-och-gora/idrott-motion-och-hallar/schemaoversikt-anlaggningar-och-lokaler?oid=253'
driver.get(url)

# Vänta tills elementet blir synligt
wait = WebDriverWait(driver, 10)
event_title_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.fc-event-title.fc-sticky')))

# Extrahera texten från elementet
event_title = event_title_element.text
print(event_title)

# Stäng webbläsaren
driver.quit()