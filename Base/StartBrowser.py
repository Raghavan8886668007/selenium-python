from selenium.webdriver import Chrome
from Library import ReadData_Configuration


def StartBrowse():
    global driver
    path = "D://python-3.6.5//chromedriver_win32 (2)//chromedriver.exe"

    driver = Chrome(executable_path=path)
    
    driver.get(ReadData_Configuration.ReadConfigData('Details','Application_URL'))
    driver.maximize_window()
    return driver

def CloseBrowser():
    driver.close()

