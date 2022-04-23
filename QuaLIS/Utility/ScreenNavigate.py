import time
from configparser import ConfigParser

from loguru import logger
from selenium.webdriver.common.by import By

from Utility import BasicOperation, LogOperation

baseMaster=ConfigParser()
baseMaster.read(BasicOperation.projectDirectory()+"\\ObjectRepository\\ElementBaseMaster.ini")

auditTrail=ConfigParser()
auditTrail.read(BasicOperation.projectDirectory()+"\\ObjectRepository\\ElementUserManagement.ini")

pin=auditTrail.get("AuditTrail", "pin")

userManagement=auditTrail.get("AuditTrail", "userManagementIcon")

master=auditTrail.get("AuditTrail","masterIcon")

auditTrail=auditTrail.get("AuditTrail", "auditTrailIcon")

sampleRegistration=ConfigParser()
sampleRegistration.read(BasicOperation.projectDirectory()+"\\ObjectRepository\\ElementSampleRegistration.ini")

def unit(driver,action):

    try:
        BasicOperation.clickXpath(driver, baseMaster.get("UnitOfMeasurement", "masterIcon"))
        logger.info("Clicked the master icon")

        LogOperation.logInfo("clicked the Master icon")
    except:

        logger.error("Unable to click the Master icon")

        LogOperation.logError("Unable to click the Master icon")

    try:
        element = driver.find_element(By.XPATH, "//span[text()='Base Master']")

        driver.execute_script("arguments[0].scrollIntoView();", element)

        element.click()

        logger.info("clicked base master icon")

        LogOperation.logInfo("clicked the Base Master icon")
    except:

        logger.error("Unable to click base master icon")

        LogOperation.logError("Unable to click the Base Master icon")

    try:

        BasicOperation.clickXpath(driver, baseMaster.get("UnitOfMeasurement", "unitOfMeasurementIcon"))


        LogOperation.logInfo("clicked the unit icon")

        logger.info("clicked the unit icon")


    except:

        logger.error("unable to click unit icon")




def auditTrailPreCondition(driver):

    try:
        BasicOperation.clickXpath(driver, master)

        LogOperation.logInfo("clicked the Master icon")

        logger.info("Clicked the master icon")

    except:
        LogOperation.logError("Unable to click the Master icon")

        logger.error("Unable to Click the master icon")


    try:
        BasicOperation.clickXpath(driver, userManagement)

        LogOperation.logInfo("clicked the User management icon")

        logger.info("clicked the User management icon")
    except:
        LogOperation.logError("Unable to click the User management icon")
        logger.error("Unable to click the User management icon")


    try:
        time.sleep(2)
        element = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div[2]/div[2]/ul/div/li[3]/div/div/a[11]")

        driver.execute_script("arguments[0].scrollIntoView();", element)

        element.click()

        LogOperation.logInfo("clicked the Audit trail icon")

        logger.info("clicked the Audit trail icon")
    except:

        logger.error("Unable to click the audit trail screen icon")

        LogOperation.logError("Unable to click the Audit trail icon")




def auditTrailPostCondition(driver):


    try:
        element = driver.find_element(By.XPATH, userManagement)

        driver.execute_script("arguments[0].scrollIntoView();", element)

        BasicOperation.clickXpath(driver, userManagement)

        LogOperation.logInfo("clicked the User management icon")

        logger.info("clicked the User management icon")
    except:
        logger.error("Unable to click the User management icon")
        LogOperation.logError("Unable to click the User management icon")









def sampleRegistration(driver):

    try:
        BasicOperation.clickXpath(driver, sampleRegistration.get("EU", "registration"))

        LogOperation.logInfo("clicked the Master icon")
    except:
        LogOperation.logError("Unable to click the Master icon")

    time.sleep(200)

    try:
        element = driver.find_element(By.XPATH, "//span[text()='Base Master']")

        driver.execute_script("arguments[0].scrollIntoView();", element)

        time.sleep(2)

        element.click()

        LogOperation.logInfo("clicked the Base Master icon")
    except:
        LogOperation.logError("Unable to click the Base Master icon")


    time.sleep(2)

    try:

        BasicOperation.scrollClickXpath(driver, baseMaster.get("UnitOfMeasurement", "unitOfMeasurementIcon"))
        LogOperation.logInfo("clicked the unit icon")
    except:

        time.sleep(2)
        try:
            BasicOperation.clickXpath(driver, baseMaster.get("UnitOfMeasurement", "unitOfMeasurementIcon"))
            LogOperation.logInfo("clicked the unit icon")
        except:
            LogOperation.logError("Unable to click the unit icon")


def storageCondition(driver):

    section="Storage Condition"

    try:
        BasicOperation.clickXpath(driver, baseMaster.get(section, "masterIcon"))

        result="clicked the Master icon"

        LogOperation.logInfo(result)

        logger.info(result)
    except:
        LogOperation.logError("Unable to click the Master icon")


    try:
        element = driver.find_element(By.XPATH, "//span[text()='Base Master']")

        driver.execute_script("arguments[0].scrollIntoView();", element)

        element.click()

        result = "clicked the Base Master icon"

        LogOperation.logInfo(result)

        logger.info(result)
    except:
        LogOperation.logError("Unable to click the Base Master icon")

    try:

        BasicOperation.clickXpath(driver, baseMaster.get(section, "storageConditionIcon"))
        result = "clicked the storage condition icon"

        LogOperation.logInfo(result)

        logger.info(result)

    except:
        LogOperation.logError("Unable to click the storage condition icon")


def containerType(driver):

    block="Container Type"

    try:
        BasicOperation.clickXpath(driver, baseMaster.get(block, "masterIcon"))

        result = "clicked the Master icon"

        LogOperation.logInfo(result)

        logger.info(result)
    except Exception as e:

        result="Unable to click the Master icon, It causes the exception "+str(e)

        LogOperation.logError(result)

        logger.error(result)


    try:
        element = driver.find_element(By.XPATH, "//span[text()='Base Master']")

        driver.execute_script("arguments[0].scrollIntoView();", element)

        element.click()


        result = "clicked the Base Master icon"

        LogOperation.logError(result)

        logger.info(result)

    except Exception as e:


        result="Unable to click the Base Master icon, , It causes the exception "+str(e)


        LogOperation.logError(result)

        logger.error(result)

    try:

        BasicOperation.clickXpath(driver, baseMaster.get(block, "containerTypeIcon"))

        result = "clicked the container type icon"

        LogOperation.logInfo(result)

        logger.info(result)
    except Exception as e:
        result = "Unable to click the container type icon, It causes the exception "+str(e)
        LogOperation.logError(result)
        logger.error(result)

