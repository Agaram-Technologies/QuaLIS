import os
import time
from configparser import ConfigParser, NoSectionError

from loguru import logger
from selenium import webdriver
from selenium.common.exceptions import SessionNotCreatedException, WebDriverException
from selenium.webdriver.common.by import By

from Utility import BasicOperation, LogOperation

projectDirectory=BasicOperation.projectDirectory()


configDriver=ConfigParser()
configDriver.read(BasicOperation.projectDirectory()+"\\config.ini")

objectRepository=ConfigParser()
objectRepository.read(projectDirectory+"\\ObjectRepository\\ElementLogin.ini")


def launchLIMS():


    try:
        driver = webdriver.Chrome(executable_path=BasicOperation.projectDirectory() + "\\chromedriver.exe")

        result="Browser Launched"

        logger.info(result)

    except SessionNotCreatedException as e:

        result ="The chrome driver is not the correct version, It causes exception-->"+str(e)

        logger.error(result)

    except Exception as e:

        result = "Unable to launch the browser it causes exception-->" + str(e)

        logger.error(result)

    driver.maximize_window()
    driver.implicitly_wait(20)

    try:
        driver.get(configDriver.get("Credential", "link"))

        result="Hit the link"

        logger.info(result)

    except NoSectionError as e:

        result ="The section is not available-->"+str(e)

        logger.error(result)

    except WebDriverException as e:

        result = "Unable to access the link, The link is not loaded-->" + str(e)

        logger.error(result)

    except Exception as e:

        result = "Unable to access the link ---> "+str(e)

        logger.error(result)


    try:
        BasicOperation.sendKeysXpath(driver, objectRepository.get("login", "loginid"),
                                     configDriver.get("Credential", "loginid"))

        logger.info("Entered the login id")

        LogOperation.logInfo("Entered Login id")

    except:
        logger.error("Unable to enter the login id")

    try:
         BasicOperation.clickXpath(driver, objectRepository.get("login", "password"))
    except:
        pass

    try:
        BasicOperation.sendKeysXpath(driver, objectRepository.get("login", "password"),
                                 configDriver.get("Credential", "password"))
        logger.info("Entered the password detail")
        LogOperation.logInfo("Entered password")
    except:
        logger.error("Unable to enter the password")


    time.sleep(1)

    try:
        BasicOperation.clickXpath(driver, objectRepository.get("login", "login"))
        logger.info("Clicked the login button")

    except:
        logger.error("Unable to click the login button")

    try:

         BasicOperation.clickXpath(driver, objectRepository.get("login", "pin"))

         result="Launch lims - Clicked the pin icon"
         LogOperation.logInfo(result)

         logger.info(result)

    except Exception as e:
         result = "Launch lims - Unable to Click the pin icon"
         logger.error(result)
         # time.sleep(5)
         # BasicOperation.clickXpath(driver, objectRepository.get("login", "pin"))

         LogOperation.logError(result)

    return driver

def refreshLogin(driver):
    driver.refresh()
    BasicOperation.sendKeysXpath(driver, objectRepository.get("login", "loginid"),
                                 configDriver.get("Credential", "loginid"))
    LogOperation.logInfo("Entered Login id")

    logger.info("Refresh-->Entered Login id")

    BasicOperation.clickXpath(driver, objectRepository.get("login", "password"))

    BasicOperation.sendKeysXpath(driver, objectRepository.get("login", "password"),
                                 configDriver.get("Credential", "password"))
    LogOperation.logInfo("Entered password id")

    logger.info("Refresh-->Entered password id")


    driver.find_element(By.XPATH, "//*[@id='nusermultirolecode']").click()

    BasicOperation.elementByText(driver, "Admin")

    driver.find_element(By.XPATH, "//*[@id='nlogintypecode']").click()

    BasicOperation.elementByText(driver, "Internal")

    BasicOperation.clickXpath(driver, objectRepository.get("login", "loginid"))

    BasicOperation.clickXpath(driver, objectRepository.get("login", "password"))

    BasicOperation.clickXpath(driver, objectRepository.get("login", "login"))

    LogOperation.logInfo("Clicked the login button")

    logger.info("Refresh-->Clicked the login button")

    try:

        BasicOperation.clickXpath(driver, objectRepository.get("login", "pin"))

        LogOperation.logInfo("Refresh Login-->, clicked pin icon")

        logger.info("Refresh Login-->, clicked pin icon")

    except Exception as e:
        print("exception")
        time.sleep(5)
        BasicOperation.clickXpath(driver, objectRepository.get("login", "pin"))

        LogOperation.logError("Refresh Login-->, Unable to click the pin icon "+str(e))

        logger.error("Refresh Login-->, Unable to click the pin icon "+str(e))




