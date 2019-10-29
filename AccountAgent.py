from time import sleep
import datetime
import Constants
import traceback
import random

def login(webdriver):
    #Open the instagram login page
    webdriver.get(Constants.URL_LOGIN)
    #sleep for 3 seconds to prevent issues with the server
    sleep(3)
    #Find username and password fields and set their input using our constants
    username = webdriver.find_element_by_name('username')
    username.send_keys(Constants.INST_USER)
    password = webdriver.find_element_by_name('password')
    password.send_keys(Constants.INST_PASS)
    #Get the login button
    button_login = webdriver.find_elements_by_class_name('btn-login')
    #sleep again
    sleep(2)
    #click login
    button_login[0].click()
    webdriver.save_screenshot(Constants.URL_SCREENSHOT+str(datetime.date.today())+".png")
    sleep(30)
    #In case you get a popup after logging in, press not now.
    #If not, then just return
    try:
        notnow = webdriver.find_element_by_css_selector(
            'body > div.RnEpo.Yx5HN > div > div > div.mt3GC > button.aOOlW.HoLwm')
        notnow.click()
    except:
        pass