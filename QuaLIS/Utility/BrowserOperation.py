import os
import time
from configparser import ConfigParser

from selenium import webdriver
from selenium.webdriver.common.by import By

from Utility import BasicOperation, LogOperation

projectDirectory=BasicOperation.projectDirectory()


configDriver=ConfigParser()
configDriver.read(BasicOperation.projectDirectory()+"\\config.ini")

objectRepository=ConfigParser()
objectRepository.read(projectDirectory+"\\ObjectRepository\\ElementLogin.ini")


def launchLIMS():
    driver = webdriver.Chrome(executable_path=BasicOperation.projectDirectory()+"\\chromedriver.exe")
    LogOperation.logInfo("Browser Launched")
    print("Browser Launched")
    driver.maximize_window()
    driver.implicitly_wait(40)
    driver.get(configDriver.get("Credential", "link"))
    LogOperation.logInfo("Link was hit")
    print("Link was hit")
    BasicOperation.sendKeysXpath(driver, objectRepository.get("login", "loginid"),
                                 configDriver.get("Credential", "loginid"))
    LogOperation.logInfo("Entered Login id")
    print("Entered Login id")



    BasicOperation.clickXpath(driver, objectRepository.get("login", "password"))

    BasicOperation.sendKeysXpath(driver, objectRepository.get("login", "password"),
                                 configDriver.get("Credential", "password"))
    LogOperation.logInfo("Entered password id")

    print("Entered password id")



    BasicOperation.clickXpath(driver, objectRepository.get("login", "login"))

    LogOperation.logInfo("Clicked the login button")

    print("Clicked the login button")

    try:

         BasicOperation.clickXpath(driver, objectRepository.get("login", "pin"))

         LogOperation.logInfo("Launch lims - Clicked the pin icon")

    except:
         print("exception")
         time.sleep(5)
         #BasicOperation.clickXpath(driver, objectRepository.get("login", "pin"))

    LogOperation.logError("Launch lims - Unable to Click the pin icon")


    return driver

def refreshLogin(driver):
    driver.refresh()
    BasicOperation.sendKeysXpath(driver, objectRepository.get("login", "loginid"),
                                 configDriver.get("Credential", "loginid"))
    LogOperation.logInfo("Entered Login id")
    print("Entered Login id")



    BasicOperation.clickXpath(driver, objectRepository.get("login", "password"))

    BasicOperation.sendKeysXpath(driver, objectRepository.get("login", "password"),
                                 configDriver.get("Credential", "password"))
    LogOperation.logInfo("Entered password id")

    print("Entered password id")



    driver.find_element(By.XPATH, "//*[@id='nusermultirolecode']").click()

    BasicOperation.elementByText(driver, "Admin")

    driver.find_element(By.XPATH, "//*[@id='nlogintypecode']").click()

    BasicOperation.elementByText(driver, "Internal")

    BasicOperation.clickXpath(driver, objectRepository.get("login", "loginid"))

    BasicOperation.clickXpath(driver, objectRepository.get("login", "password"))

    BasicOperation.clickXpath(driver, objectRepository.get("login", "login"))

    LogOperation.logInfo("Clicked the login button")

    print("Clicked the login button")

    try:

        BasicOperation.clickXpath(driver, objectRepository.get("login", "pin"))

        LogOperation.logInfo("Refresh Login-->, clicked pin icon")

    except Exception as e:
        print("exception")
        time.sleep(5)
        BasicOperation.clickXpath(driver, objectRepository.get("login", "pin"))

        LogOperation.logError("Refresh Login-->, Unable to click the pin icon "+str(e))




