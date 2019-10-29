from selenium import webdriver
import BotEngine
import Constants

chromedriver_path = "/Users/jmurillocordoba/Downloads/chromedriver"
webdriver = webdriver.Chrome(executable_path=chromedriver_path)

BotEngine.init(webdriver)
BotEngine.update(webdriver)

webdriver.close()