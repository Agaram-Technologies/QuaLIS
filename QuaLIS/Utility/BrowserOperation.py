import os
import time
from configparser import ConfigParser

from selenium import webdriver
from selenium.webdriver.common.by import By

from Utility import BasicOperation, LogOperation

projectDirectory=BasicOperation.projectDirectory()


configDriver=ConfigParser()
configDriver.read("..\config.ini")

objectRepository=ConfigParser()
objectRepository.read(projectDirectory+"\\ObjectRepository\\ElementLogin.ini")



def launchLIMS():
    driver = webdriver.Chrome(executable_path="..\chromedriver.exe")
    LogOperation.logInfo("Browser Launched")
    print("Browser Launched")
    driver.maximize_window()
    driver.implicitly_wait(20)
    driver.get(configDriver.get("Credential", "link"))
    LogOperation.logInfo("Link was hit")
    print("Link was hit")

    BasicOperation.sendKeysXpath(driver, objectRepository.get("login", "loginid"),
                                 configDriver.get("Credential", "loginid"))
    LogOperation.logInfo("Entered Login id")
    print("Entered Login id")

    time.sleep(2)

    BasicOperation.clickXpath(driver, objectRepository.get("login", "password"))

    BasicOperation.sendKeysXpath(driver, objectRepository.get("login", "password"),
                                 configDriver.get("Credential", "password"))
    LogOperation.logInfo("Entered password id")

    print("Entered password id")

    time.sleep(2)

    BasicOperation.clickXpath(driver, objectRepository.get("login", "login"))

    LogOperation.logInfo("Clicked the login button")

    print("Clicked the login button")

    time.sleep(5)

    url = driver.current_url

    if url == "http://192.168.0.199:9091/QuaLISWeb/#/home":
        print("logged in")
    else:
         BasicOperation.clear(driver, objectRepository.get("login", "loginid"))
         BasicOperation.sendKeysXpath(driver, objectRepository.get("login", "loginid"),
                                  configDriver.get("Credential", "loginid"))

         BasicOperation.clickXpath(driver, objectRepository.get("login", "password"))

         BasicOperation.clear(driver, objectRepository.get("login", "password"))
         BasicOperation.sendKeysXpath(driver, objectRepository.get("login", "password"),
                                                         configDriver.get("Credential", "password"))
         LogOperation.logInfo("Entered password id")

         print("Entered password id")

         time.sleep(1)

         #BasicOperation.clickXpath(driver, objectRepository.get("login", "userRole"))

         driver.find_element(By.XPATH, "//*[@id='nusermultirolecode']").click()

         BasicOperation.elementByText(driver, "Admin")

         driver.find_element(By.XPATH, "//*[@id='nlogintypecode']").click()

         BasicOperation.elementByText(driver, "Internal")

         BasicOperation.clickXpath(driver, objectRepository.get("login", "login"))

    return driver




















