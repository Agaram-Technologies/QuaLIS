import time
from configparser import ConfigParser

from selenium.webdriver.common.by import By

from TestCoverage import TestCoverageAudittrail
from Utility import BasicOperation, ScreenNavigate, BrowserOperation, ResultFlag
from Utility.BrowserOperation import configDriver
baseMaster=ConfigParser()
baseMaster.read(BasicOperation.projectDirectory()+"\\ObjectRepository\\ElementBaseMaster.ini")

def unitAdd(driver,name,description):
    ScreenNavigate.unit(driver)

    BasicOperation.clickXpath(driver, baseMaster.get("UnitOfMeasurement", "unitAdd"))

    BasicOperation.sendKeysXpath(driver, baseMaster.get("UnitOfMeasurement", "unitName"), name)

    BasicOperation.sendKeysXpath(driver, baseMaster.get("UnitOfMeasurement", "unitDescription"),
                                 description)

    BasicOperation.clickXpath(driver,
                              baseMaster.get("UnitOfMeasurement", "unitAddSubmit"))

    BrowserOperation.refreshLogin(driver)


def unitEdit(driver):
    ScreenNavigate.unit(driver)

def unitDelete(driver,name):
    ScreenNavigate.unit(driver)
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

    BasicOperation.clickXpath(driver, baseMaster.get("UnitOfMeasurement", "UnitDeleteConfirmationOK"))

    time.sleep(7)

    q = driver.find_elements(By.TAG_NAME, "tr")
    qq = len(q)

    # input("enter containertype with description: ")
    container = "vial + syringe"
    for i in range(1, qq):
        qqq = q[i].text
        print(qqq)
        if container == qqq:
            print("containertype count is", i, qqq)
            print(i)
            m = str(i)
            delete = "(//span[@data-tip='Delete'])[" + m + "]"
            print(delete)
            driver.find_element(By.XPATH, delete).click()
            break





def auditTrailUnitAdd(driver,name,description):

    ResultCase1="Unexecuted"


    # Case1 about increase the number of data or not
    case1="Unexecuted"

    # Case2 about increase the number of data or not by 1
    case2="Unexecuted"

    # Case2 about increase the number of data or not by more than 1
    case3="Unexecuted"

    beforeCount=TestCoverageAudittrail.auditTrailRecordCount()

    unitAdd(driver,name,description)

    afterCount=TestCoverageAudittrail.auditTrailRecordCount()


    if afterCount==beforeCount:
        case1=ResultFlag.failFlag
        case2=ResultFlag.failFlag
        case3=ResultFlag.failFlag

    elif afterCount==beforeCount+1:
        case2=ResultFlag.passFlag
        case1=ResultFlag.passFlag
        case3=ResultFlag.passFlag

    elif afterCount>beforeCount+1:
        case3=ResultFlag.failFlag
        case1=ResultFlag.passFlag
        case2=ResultFlag.failFlag


