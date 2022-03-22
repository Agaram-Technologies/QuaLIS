import time
from configparser import ConfigParser

from selenium.webdriver.common.by import By

from Utility import BasicOperation

baseMaster=ConfigParser()
baseMaster.read(BasicOperation.projectDirectory()+"\\ObjectRepository\\ElementBaseMaster.ini")

auditTrail=ConfigParser()
auditTrail.read(BasicOperation.projectDirectory()+"\\ObjectRepository\\ElementUserManagement.ini")

pin=auditTrail.get("AuditTrail", "pin")

userManagement=auditTrail.get("AuditTrail", "userManagementIcon")

master=auditTrail.get("AuditTrail","masterIcon")

auditTrail=auditTrail.get("AuditTrail", "auditTrailIcon")

def unit(driver):

    BasicOperation.clickXpath(driver, baseMaster.get("UnitOfMeasurement", "masterIcon"))

    element = driver.find_element(By.XPATH, "//span[text()='Base Master']")

    driver.execute_script("arguments[0].scrollIntoView();", element)

    element.click()

    try:

        BasicOperation.scrollClickXpath(driver, baseMaster.get("UnitOfMeasurement", "unitOfMeasurementIcon"))

    except:
        BasicOperation.clickXpath(driver, baseMaster.get("UnitOfMeasurement", "unitOfMeasurementIcon"))


def auditTrailPreCondition(driver):

    BasicOperation.clickXpath(driver, master)

    BasicOperation.clickXpath(driver, userManagement)

    element = driver.find_element(By.XPATH,"//a[@href='#/audittrail' and @nformcode='78' and text()='Audit Trail']")

    driver.execute_script("arguments[0].scrollIntoView();", element)

    time.sleep(2)

    element.click()


def auditTrailPostCondition(driver):
    element = driver.find_element(By.XPATH, userManagement)

    driver.execute_script("arguments[0].scrollIntoView();", element)

    BasicOperation.clickXpath(driver, userManagement)