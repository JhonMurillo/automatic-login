from selenium import webdriver
import BotEngine
import Constants
import sys
path=''

try:
    if sys.argv[1] == 'path':
        path = '../'
except:
    pass

chromedriver_path = "/Users/jmurillocordoba/Downloads/chromedriver"
webdriver = webdriver.Chrome(executable_path=chromedriver_path)

BotEngine.init(webdriver, path)
webdriver.close()