from time import sleep
from webbrowser import Chrome
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions

def send2inputelm(by,key,value):
  elm = driver.find_element(by=by, value=key)
  elm.send_keys(value)

fb_username = 
fb_password = 

options = ChromeOptions()

#options.add_argument("--headless")

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
driver.get("https://www.facebook.com/")
print("Facebook is ready.")

send2inputelm(by=By.ID, key="email", value=fb_username)
send2inputelm(by=By.ID, key="pass", value=fb_password)

login_btn_elm = driver.find_element(by=By.NAME, value="login")
login_btn_elm.click()

print("Login Succeeded")

driver.implicitly_wait(1)

open_messenger_btn_elm = driver.find_element(by=By.CSS_SELECTOR, value='[aria-label="Messenger"]')
open_messenger_btn_elm.click()

driver.implicitly_wait(1)

chat_elm = driver.find_element(by=By.CSS_SELECTOR, value='[aria-label="チャット"]')

messenger_room_elms = chat_elm.find_elements(by=By.CSS_SELECTOR, value='[data-testid="mwthreadlist-item-open"]')

room_names = []

for room in messenger_room_elms:
  name_span_elm = room.find_element(by=By.CSS_SELECTOR, value='span span')
  room_names.append(name_span_elm.text)

driver.get("https://www.facebook.com/messages/t/8039099789435262")

driver.implicitly_wait(100)

driver.quit()

print("Application Closed")