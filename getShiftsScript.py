from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import StaleElementReferenceException


import time
# # Set up the WebDr
# # iver
# service = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=service)
#
# # Open the webpage
# driver.get('https://app.ezshift.co.il/pages/loginHE-il.aspx')
#
# # Locate and fill the login form fields
# username_field = driver.find_element(By.NAME, 'Username')
# password_field = driver.find_element(By.NAME, 'Password')
# company_field = driver.find_element(By.NAME, 'Company')
# login_button = driver.find_element(By.NAME, '_ctl1')
#
# username_field.send_keys('alexander.tsiganenko@intel.com')
# password_field.send_keys('Zxwe34ui!')
# company_field.send_keys('intel')
# login_button.click()
#
# driver.get('https://app.ezshift.co.il/pages/ScheduleMy.aspx')
# time.sleep(1.5)
# # Wait for the dynamic content to load
# WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ShiftsTable')))
#
# # Locate the table
# table = driver.find_element(By.ID, 'ShiftsTable')
# print('wtf?1')
# print(table)
# print('wtf?')
#  # Extract the data
# rows = table.find_elements(By.TAG_NAME, 'tr')
# for row in rows:
#      tds = row.find_elements(By.TAG_NAME, 'td')
#
#      if len(tds) >= 2:
#          print(tds[1].text)
#          print(tds[2].text)
#
#  # Clean up (close the browser)
# driver.quit()

def trigger_click(element):
    element.click()

def select_missing_days(driver):

    day= '4' #test
    missing_days_selector = '.dayImageNumberContainer'
    missing_days_button = 'ctl00_mp_RefreshSelectedDays'

    missing_day_elements = driver.find_elements(By.CSS_SELECTOR, missing_days_selector)
    for el in missing_day_elements:
        dayNumber=el.find_element(By.CLASS_NAME, "dTS").text
        if(dayNumber==day):
            trigger_click(el)

    missing_days_button_element = driver.find_element(By.ID, missing_days_button)
    trigger_click(missing_days_button_element)
    fill_work_time(driver, '09:00', '18:30')

def fill_work_time(driver, start_time, end_time):
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'tbody > tr[id*="EmployeeReports"]'))
    )
    schedule_elements = driver.find_elements(By.CSS_SELECTOR, 'tbody > tr[id*="EmployeeReports"]')

    for row in schedule_elements:
        try:
            # Locate the dropdown each time in the loop to avoid stale references
            select_element = Select(row.find_element(By.CSS_SELECTOR, 'td > select[id*="ctl00_mp_RG_Days"]'))
            select_element.select_by_value('4')
        except StaleElementReferenceException:
            # If stale element exception caught, break the loop or continue as per your logic
            continue
        except Exception as e:
            print(f"An error occurred: {e}")
        print("dsfsf")
    print("enf")


def fill_days():
    # options = Options()
    # options.add_argument("--headless")  # Run in headless mode (no GUI)
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    log_in(driver)
    time.sleep(1.5)  # Sleep for 1.5 seconds
    driver.get("https://intel.net.hilan.co.il/Hilannetv2/Attendance/calendarpage.aspx?itemId=47")  # Replace with the URL you want to interact with
    select_missing_days(driver)

   # driver.quit()  # Close the WebDriver when done
def log_in(driver):
    driver.get("https://intel.net.hilan.co.il/login")
    username_field = driver.find_element(By.ID, 'user_nm')
    password_field = driver.find_element(By.ID, 'password_nm')
    login_button = driver.find_element(By.CSS_SELECTOR, "button.hbutton2.hbutton2-lg.primary.fw.mb")

    username_field.send_keys('********')
    password_field.send_keys('********')
    login_button.click()

fill_days()
