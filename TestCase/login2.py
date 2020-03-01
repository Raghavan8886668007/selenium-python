from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select

path = "D://python-3.6.5//chromedriver_win32 (2)//chromedriver.exe"
driver = Chrome(executable_path=path)
driver.get("https://www.thetestingworld.com/testings/")
driver.maximize_window()
driver.find_element_by_xpath("//label[@for='tab2']").click()
driver.find_element_by_xpath("//input[@name='_txtUserName']").send_keys("Akhil123")
driver.find_element_by_xpath("//input[@name='_txtPassword']").send_keys("Akhil@007")
driver.find_element_by_xpath("//input[@value='Login']").click()
driver.find_element_by_xpath("//a[contains(text(), 'My Account')]").click()
driver.find_element_by_xpath("//a[contains(text(), 'Update')]").click()
drive = driver.window_handles
print(drive)
driver.find_element_by_xpath("//a[contains(text(),'thetestingworld.com')]").click()
drivers = driver.window_handles
print(drivers)

for win in drivers:
    driver.switch_to.window(win)
    print(driver.current_url)

