from Library import ReadData_Configuration

class  Registration:

    def __init__(self,obj):
        global driver
        driver = obj

    def username(self,username):
        driver.find_element_by_xpath(ReadData_Configuration.ReadConfigData('Details', 'username')).send_keys(username)

    def email(self,email):
        driver.find_element_by_xpath(ReadData_Configuration.ReadConfigData('Details', 'email')).send_keys(email)

    def password(self,password):
        driver.find_element_by_xpath(ReadData_Configuration.ReadConfigData('Details', 'password')).send_keys(password)

    def cfnpassword(self,cfnpassword):
        driver.find_element_by_xpath(ReadData_Configuration.ReadConfigData('Details', 'confirm password')).send_keys(cfnpassword)

    def dob(self,dob):
        driver.find_element_by_xpath(ReadData_Configuration.ReadConfigData('Details', 'dob')).send_keys(dob)

    def phone(self,phone):
        driver.find_element_by_xpath(ReadData_Configuration.ReadConfigData('Details', 'phone')).send_keys(phone)

    def address(self,address):
        driver.find_element_by_xpath(ReadData_Configuration.ReadConfigData('Details', 'address')).send_keys(address)

    def radioButton(self):
        radios = driver.find_elements_by_xpath(ReadData_Configuration.ReadConfigData('Details', 'radio'))
        for i in range(len(radios)):
            print(i)
            print(radios[i])
            #pprint(radios(i).text)


