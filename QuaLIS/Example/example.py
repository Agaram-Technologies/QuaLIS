from configparser import ConfigParser

from Utility import BrowserOperation, BasicOperation

driver=BrowserOperation.launchLIMS()

objectRepository=ConfigParser()
objectRepository.read("D:\\Agaram Technologies\\Github\\QuaLIS\\ObjectRepository\\ElementLogin.ini")

BasicOperation.exceptionClick(driver, objectRepository.get("login", "pin"))