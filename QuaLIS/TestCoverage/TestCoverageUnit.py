import time

from selenium.webdriver.common.by import By

from Utility import BasicOperation, ScreenNavigate
from Utility.BrowserOperation import configDriver


def unitAdd(driver,name,description):
    ScreenNavigate.unit(driver)

def unitEdit(driver):
    ScreenNavigate.unit(driver)

def unitDelete(driver,name):
    unitNameList = driver.find_elements(By.XPATH,
                                        "/html/body/div[1]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[3]/div/div[1]/table/tbody/tr/td[1]")

    unitDeleteLit = driver.find_elements(By.XPATH,
                                         "/html/body/div[1]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[3]/div/div[1]/table/tbody/tr/td[4]/a/span[2]")

    unitNameLists = []

    for i in unitNameList:
        unitName = i.text
        unitNameLists.append(unitName)

    for i in unitNameLists:

        if i == name:
            index = unitNameLists.index(i)

            unitDeleteLit[index].click()

    time.sleep(3)

    BasicOperation.clickXpath(driver, configDriver.get("UnitOfMeasurement", "UnitDeleteConfirmationOK"))


