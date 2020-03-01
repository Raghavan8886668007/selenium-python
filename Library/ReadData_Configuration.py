import configparser

def ReadConfigData(section,key):
    config = configparser.ConfigParser()
    config.read("C://Users//ssrivathsan//AppData//Local//Programs//Python//Python36//Frameworks//ConfigurationData//Config.cfg")
    return config.get(section,key)
