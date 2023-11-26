# import requests
# from bs4 import BeautifulSoup as bs

# #url = "https://app.ezshift.co.il/pages/ScheduleMy.aspx"
# #r = requests.get(url)
# #r.raise_for_status()

# session= requests.Session()

# auth_html= session.get("https://app.ezshift.co.il/pages/loginHE-il.aspx")
# auth_bs=bs(auth_html.content,'html.parser')
# view_state=auth_bs.select("input[name=__VIEWSTATE]")[0]['value']
# view_state_generator=auth_bs.select("input[name=__VIEWSTATEGENERATOR]")[0]['value']
# event_validation_state=auth_bs.select("input[name=__EVENTVALIDATION]")[0]['value']

# payload = {
#     '__VIEWSTATE': view_state,
#     '__VIEWSTATEGENERATOR': view_state_generator ,
#     '__EVENTVALIDATION': event_validation_state,
#     'Username': 'alexander.tsiganenko@intel.com',
#     'Password': 'Zxwe34ui!',
#     'Company': 'intel',
#     'remember': 'on',
#     '_ctl1': 'התחבר'
# }      
# session.post('https://app.ezshift.co.il/pages/loginHE-il.aspx', data=payload)

# response = session.post('https://app.ezshift.co.il/pages/ScheduleMy.aspx')
# html = bs(response.text, 'html.parser')

# table =html.find('table', id='ShiftsTable')
# rows = table.find_all('tr')


# print(rows)
# #html = bs(r.text, 'html.parser')
# #print(html.select(".card"))
# #for el in html.select("._default-grid_vrdym_258 > ._card_6bcao_1"):
#  #   title = el.select('._card_6bcao_1 > a')
#   #  if title:
#    #     print(title[0].text)

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
# Set up the WebDr
# iver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Open the webpage
driver.get('https://app.ezshift.co.il/pages/loginHE-il.aspx')

# Locate and fill the login form fields
username_field = driver.find_element(By.NAME, 'Username')
password_field = driver.find_element(By.NAME, 'Password')
company_field = driver.find_element(By.NAME, 'Company')
login_button = driver.find_element(By.NAME, '_ctl1')

username_field.send_keys('alexander.tsiganenko@intel.com')
password_field.send_keys('Zxwe34ui!')
company_field.send_keys('intel')
login_button.click()

driver.get('https://app.ezshift.co.il/pages/ScheduleMy.aspx')
time.sleep(1.5) 
# Wait for the dynamic content to load
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ShiftsTable')))

# Locate the table
table = driver.find_element(By.ID, 'ShiftsTable')
print('wtf?1')
print(table)
print('wtf?')
 # Extract the data
rows = table.find_elements(By.TAG_NAME, 'tr')
for row in rows:
     tds = row.find_elements(By.TAG_NAME, 'td')

     if len(tds) >= 2:
         print(tds[1].text)
         print(tds[2].text)

 # Clean up (close the browser)
driver.quit()
