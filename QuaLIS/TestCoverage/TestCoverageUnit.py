import time
from configparser import ConfigParser

from selenium.webdriver.common.by import By

from TestCoverage import TestCoverageAudittrail
from Utility import BasicOperation, ScreenNavigate, BrowserOperation, ResultFlag, LogOperation, ExceptionHandling
from Utility.BrowserOperation import configDriver
baseMaster=ConfigParser()
baseMaster.read(BasicOperation.projectDirectory()+"\\ObjectRepository\\ElementBaseMaster.ini")

def unitAdd(driver,name,description,defaultStatus):

    time.sleep(2)

    ScreenNavigate.unit(driver)

    time.sleep(2)

    ExceptionHandling.exceptionClick(driver,baseMaster.get("UnitOfMeasurement", "unitAdd"),"Clicked the Unit add button", "Unable to click the unit add button")

    BasicOperation.clickXpath(driver, )
    time.sleep(2)
    BasicOperation.sendKeysXpath(driver, baseMaster.get("UnitOfMeasurement", "unitName"), name)
    time.sleep(2)
    BasicOperation.sendKeysXpath(driver, baseMaster.get("UnitOfMeasurement", "unitDescription"),
                                 description)
    time.sleep(2)
    BasicOperation.clickXpath(driver,
                              baseMaster.get("UnitOfMeasurement", "unitAddSubmit"))
    time.sleep(2)
    element = driver.find_element(By.XPATH, "//span[text()='Base Master']")
    time.sleep(2)
    try:
        driver.execute_script("arguments[0].scrollIntoView();", element)
    except:
        pass
    time.sleep(2)
    element.click()
    time.sleep(2)


def unitDelete(driver,name,description,defaultStatus):
    ScreenNavigate.unit(driver)

    q = driver.find_elements(By.TAG_NAME, "tr")
    qq = len(q)

    # input("enter containertype with description: ")
    unit = name+" "+description+" "+defaultStatus
    for i in range(1, qq):
        unitrow = q[i].text

        if unit.__contains__(name):
            print("unit delete Matched at "+str(i))
            print("unit count is", i, unitrow)
            print(i)
            m = str(i)
            delete = "(//span[@data-tip='Delete'])[" + m + "]"
            print(delete)
            driver.find_element(By.XPATH, delete).click()

            driver.find_element(By.XPATH,"//*[text()='OK']").click()

            break

        else:
            print("Not matched")


def unitEdit(driver,oldName,oldDescription,oldDefaultStatus,newName,newDescription):
    ScreenNavigate.unit(driver)

    q = driver.find_elements(By.TAG_NAME, "tr")
    qq = len(q)

    # input("enter containertype with description: ")
    container = oldName + " " + oldDescription + " " + oldDefaultStatus
    for i in range(1, qq):
        unitrow = q[i].text

        print("unitrow "+unitrow)

        print(container)



        if unitrow.__contains__(oldName):
            print("unit edit Matched at " + str(i))
            print("containertype count is", i, unitrow)
            print(i)
            m = str(i)
            edit = "(//span[@data-tip='Edit'])[" + m + "]"

            driver.find_element(By.XPATH, edit).click()



            BasicOperation.clear(driver, baseMaster.get("UnitOfMeasurement", "unitDescription"))

            BasicOperation.clear(driver, baseMaster.get("UnitOfMeasurement", "unitName"))

            time.sleep(2)

            BasicOperation.clear(driver, baseMaster.get("UnitOfMeasurement", "unitDescription"))


            BasicOperation.sendKeysXpath(driver, baseMaster.get("UnitOfMeasurement", "unitName"), newName)
            time.sleep(2)

            # BasicOperation.sendKeysXpath(driver, baseMaster.get("UnitOfMeasurement", "unitDescription"),
                                         #newDescription)
            time.sleep(2)
            BasicOperation.clickXpath(driver,
                                      baseMaster.get("UnitOfMeasurement", "unitEditSubmit"))

            time.sleep(2)

            break

        else:
            print("Not matched")






def auditTrailUnitAdd(driver,name,description,defaultStatus):

    ResultCase1="Unexecuted"

    beforeCount=TestCoverageAudittrail.auditTrailRecordCount(driver)

    print("once the count get")
    print(beforeCount)

    auditTrailRecord={"AuditAction":"ADD UNIT","comments":"Unit Name: {};Description: {};Default Status: No;".format(name,description),"userName":"Carl Dolman","userRole":"Admin","ActionType":"SYSTEM","ModuleName":"Base Master","FormName":"Unit of Measurement","esignComments":""}



    unitAdd(driver,name,description)

    afterCount=TestCoverageAudittrail.auditTrailRecordCount(driver)

    # print(afterCount)



    if afterCount==beforeCount:
        ResultCase1="FAIL"

        print("Audit trail is not captured")

    elif afterCount==beforeCount+1:
        ResultCase1 = "PASS"

        print("Audit trail is captured")

        auditDateAndTime=driver.find_element(By.XPATH,"//tbody[@role='presentation']/tr[2]/td[2]").text

        print("Date and Time - "+auditDateAndTime)

        auditAction = driver.find_element(By.XPATH, "//tbody[@role='presentation']/tr[2]/td[3]").text

        print("Audit Action - "+auditAction)

        if auditAction==auditTrailRecord.get("AuditAction"):
            print("Audit action is properly mentioned")

        else:
            print("Audit action is not properly mentioned")

        comments = driver.find_element(By.XPATH, "//tbody[@role='presentation']/tr[2]/td[4]").text

        expectedComments=auditTrailRecord.get("comments")

        if comments==expectedComments:
            print("Comment is properly displayed")

        else:
            print("Comment is not displaying properly")

        print("Comments - "+comments)

        userName = driver.find_element(By.XPATH, "//tbody[@role='presentation']/tr[2]/td[5]").text

        expectedUserName=auditTrailRecord.get("userName")

        if userName==expectedUserName:
            print("user name is properly displayed")

        else:
            print("user name is not displaying properly")

        print("User Name - "+userName)
        userRole = driver.find_element(By.XPATH, "//tbody[@role='presentation']/tr[2]/td[6]").text

        expectedUserName = auditTrailRecord.get("userRole")

        if userRole == expectedUserName:
            print("user role is properly displayed")

        else:
            print("user role is not displaying properly")
        print("User Role - "+userRole)
        actionType = driver.find_element(By.XPATH, "//tbody[@role='presentation']/tr[2]/td[7]").text

        expectedActionType= auditTrailRecord.get("actionType")

        if actionType == expectedActionType:
            print("Action type is properly displayed")

        else:
            print("Action type is not displaying properly")

        print("Action type - "+actionType)
        moduleName = driver.find_element(By.XPATH, "//tbody[@role='presentation']/tr[2]/td[8]").text

        expectedModuleName = auditTrailRecord.get("moduleName")

        if expectedModuleName == moduleName:
            print("Module name  is properly displayed")

        else:
            print("Module name   is not displaying properly")
        print("Module Name - "+moduleName)
        formName = driver.find_element(By.XPATH, "//tbody[@role='presentation']/tr[2]/td[9]").text

        expectedFormName = auditTrailRecord.get("formName")

        if formName == expectedFormName:
            print("Form name is properly displayed")

        else:
            print("Form name is not displaying properly")
        print("Form Name - "+formName)
        esignComments = driver.find_element(By.XPATH, "//tbody[@role='presentation']/tr[2]/td[10]").text
        expectedEsignComments = auditTrailRecord.get("esignComments")

        if esignComments == expectedEsignComments:
            print("Esign comment is properly displayed")

        else:
            print("AEsign comment  is not displaying properly")
        print("Esign comments"+esignComments)
    elif afterCount>beforeCount+1:
         ResultCase1 = "PASS-More than one record is available"






    #print(ResultCase1)


def downloadPDF(driver):
    time.sleep(2)
    ScreenNavigate.unit(driver)
    time.sleep(2)

    try:
        BasicOperation.clickXpath(driver,   baseMaster.get("UnitOfMeasurement", "unitDownloadPDF"))
        LogOperation.logInfo("Clicked the Download PDF button")
    except Exception as e:
        LogOperation.logError(
            "Unable to click the Download PDF button, It causes the exception, Exception Detail---> " + str(e))

    try:
        element = driver.find_element(By.XPATH, "//span[text()='Base Master']")
        time.sleep(2)
        try:
            driver.execute_script("arguments[0].scrollIntoView();", element)
        except:
            pass
        time.sleep(2)
        element.click()
        time.sleep(2)
        LogOperation.logInfo("Clicked the basemaster icon")

    except Exception as e:
        LogOperation.logError("Unable to click the basemaster icon -- post condition, It causes exception-->" + str(e))


def downloadExcel(driver):
    time.sleep(2)
    ScreenNavigate.unit(driver)
    time.sleep(2)
    try:
        BasicOperation.clickXpath(driver,   baseMaster.get("UnitOfMeasurement", "unitDownloadExcel"))
        LogOperation.logInfo("Clicked the Download Excel button")
    except Exception as e:
        LogOperation.logError("Unable to click the Download excel button, It causes the exception, Exception Detail---> "+str(e))

        time.sleep(2)

        try:
            element = driver.find_element(By.XPATH, "//span[text()='Base Master']")
            time.sleep(2)
            try:
                driver.execute_script("arguments[0].scrollIntoView();", element)
            except:
                pass
            time.sleep(2)
            element.click()
            time.sleep(2)
            LogOperation.logInfo("Clicked the basemaster icon")

        except Exception as e:
            LogOperation.logError("Unable to click the basemaster icon -- post condition, It causes exception-->"+str(e))








def unitFilter(driver):

        ScreenNavigate.unit(driver)

        BasicOperation.clickXpath(driver, baseMaster.get("UnitOfMeasurement", "unitNameFilter"))

        driver.find_element(By.XPATH,"(//span[@role='listbox'])[2]").click()

        driver.implicitly_wait(3)

        d= driver.find_elements(By.XPATH,"(//span[@role='listbox'])[2]/*[1]/*")

        print(len(d))




#driver=BrowserOperation.launchLIMS()

#unitFilter(driver)