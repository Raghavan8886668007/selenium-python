from selenium.webdriver import Chrome
from Base import StartBrowser
from Library import ReadData_Configuration
from POM import RegistrationPage
def test_Registration():
    driver = StartBrowser.StartBrowse()
    register = RegistrationPage.Registration(driver)
    register.username("admin007")
    register.email("admin@gmail.com")
    register.password("test123")
    register.cfnpassword("test123")
    register.dob("02/21/2020")
    register.phone("9087654321")
    register.address("10 downing street")
    register.radioButton()



