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

    element = driver.find_element(By.XPATH, "//span[text()='Base Master']")

    try:
        driver.execute_script("arguments[0].scrollIntoView();", element)
    except:
        pass

    element.click()


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

    beforeCount=TestCoverageAudittrail.auditTrailRecordCount(driver)



    print("once the count get")
    print(beforeCount)

    # unitAdd(driver,name,description)

    #  afterCount=TestCoverageAudittrail.auditTrailRecordCount(driver)

    # print(afterCount)

    afterCount=beforeCount+1

    if afterCount==beforeCount:
        ResultCase1="FAIL"

    elif afterCount==beforeCount+1:
        ResultCase1 = "PASS"

        auditDateAndTime=driver.find_element(By.XPATH,"//tbody[@role='presentation']/tr[2]/td[2]").text

        print("Date and Time - "+auditDateAndTime)

        auditAction = driver.find_element(By.XPATH, "//tbody[@role='presentation']/tr[2]/td[3]").text

        print("Audit Action - "+auditAction)

        comments = driver.find_element(By.XPATH, "//tbody[@role='presentation']/tr[2]/td[4]").text

        print("Comments - "+comments)

        userName = driver.find_element(By.XPATH, "//tbody[@role='presentation']/tr[2]/td[5]").text

        print("User Name - "+userName)
        userRole = driver.find_element(By.XPATH, "//tbody[@role='presentation']/tr[2]/td[6]").text

        print("User Role - "+userRole)
        actionType = driver.find_element(By.XPATH, "//tbody[@role='presentation']/tr[2]/td[7]").text

        print("Action type - "+actionType)
        moduleName = driver.find_element(By.XPATH, "//tbody[@role='presentation']/tr[2]/td[8]").text

        print("Module Name - "+moduleName)
        formName = driver.find_element(By.XPATH, "//tbody[@role='presentation']/tr[2]/td[9]").text

        print("Form Name - "+formName)
        esignComments = driver.find_element(By.XPATH, "//tbody[@role='presentation']/tr[2]/td[10]").text

        print("Esign comments"+esignComments)
    elif afterCount>beforeCount+1:
         ResultCase1 = "PASS-More than one record is available"






    #print(ResultCase1)