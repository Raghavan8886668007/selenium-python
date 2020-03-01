from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as ec
from selenium.webdriver.common.by import By

import time
path = "D://python-3.6.5//chromedriver_win32 (2)//chromedriver.exe"
driver = Chrome(executable_path=path)
driver.get("https://www.thetestingworld.com/testings/")
driver.maximize_window()
#driver.implicitly_wait(20)
driver.execute_script("window.scrollTo(0, 500)")
radio = driver.find_elements_by_xpath("//input[@name='add_type']")
print(radio)
print(len(radio))
for radios in range(len(radio)):
    print(radio[radios].text)
#dropdowns
drives= Select(driver.find_element_by_xpath("//select[@id='countryId']"))
int = drives.options
print(len(int))
for option in range(len(int)):
    country = (int[option].text)
    if("Yugoslavia"==country):
        drives.select_by_index(option)
time.sleep(6)
#wait = WebDriverWait(driver, 100)
#wait.until(ec.text_to_be_present_in_element((By.XPATH, "stateId"), "Vojvodina"))

print("1")
drive = Select(driver.find_element_by_xpath("//select[@id='stateId']"))
print("2")
driverss = drive.options
for driver in range(len(driverss)):
    state = (driverss[driver].text)
    print("3")
    if("Vojvodina"==state):
       print("4")
       drive.select_by_index(driver)

time.sleep(6)
print("344")
city = Select(driver.find_element_by_xpath("//select[@id='cityId']"))
city.select_by_index(7)







