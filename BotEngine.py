import Constants
import AccountAgent

def init(webdriver, path):
    Constants.init(path)
    AccountAgent.login(webdriver)


def update(webdriver):
    return