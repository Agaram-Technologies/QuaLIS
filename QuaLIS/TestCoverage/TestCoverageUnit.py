
import keyboard
import time
from configparser import ConfigParser

from selenium.webdriver.common.by import By

from ObjectRepository import ElementAuditTrail
from TestCoverage import TestCoverageAudittrail
from Utility import BasicOperation, ScreenNavigate, BrowserOperation, ResultFlag, LogOperation, ExceptionHandling
from Utility.BrowserOperation import configDriver
baseMaster=ConfigParser()
baseMaster.read(BasicOperation.projectDirectory()+"\\ObjectRepository\\ElementBaseMaster.ini")

def unitAdd(driver,name,description,defaultStatus):

    time.sleep(2)

    ScreenNavigate.unit(driver)

    countListbefore=driver.find_element(By.XPATH,baseMaster.get("UnitOfMeasurement", "unitCount")).text

    countLIST=countListbefore.split(' ')

    beforeCount=countLIST[4]

    print("before count-->"+str(beforeCount))

    time.sleep(2)

    ExceptionHandling.exceptionClick(driver,baseMaster.get("UnitOfMeasurement", "unitAdd"),"Clicked the Unit add button", "Unable to click the unit add button")

    time.sleep(2)
    ExceptionHandling.exceptionSendKeys(driver, baseMaster.get("UnitOfMeasurement", "unitName"), name,"Entered the unit name", "Unable to enter the unit name")


    time.sleep(2)

    ExceptionHandling.exceptionSendKeys(driver, baseMaster.get("UnitOfMeasurement", "unitDescription"), name,"Entered the unit description", "Unable to enter the unit description")

    time.sleep(2)


    if defaultStatus=="Yes":


        defaultStatusToggle=driver.find_element(By.XPATH,baseMaster.get("UnitOfMeasurement", "unitDefaultStatusToggle"))

        if defaultStatusToggle.get_attribute("value")=="false":
            ExceptionHandling.exceptionClick(driver, baseMaster.get("UnitOfMeasurement", "unitDefaultStatus"),"Clicked the default status button","Unable to click the default status")




    ExceptionHandling.exceptionClick(driver,
                              baseMaster.get("UnitOfMeasurement", "unitAddSubmit"),"Clicked the add submit button","unable to click the add submit button")

    time.sleep(2)

    countListafter = driver.find_element(By.XPATH, baseMaster.get("UnitOfMeasurement", "unitCount")).text

    aftercountLIS = countListafter.split(' ')

    afterCount = aftercountLIS[4]

    print("afterCount-->" + afterCount)

    if int(afterCount)==int(beforeCount)+1:
        print("unit added successfully")

    else:
        print("Unit add is not working properly")

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

    countListbefore = driver.find_element(By.XPATH, baseMaster.get("UnitOfMeasurement", "unitCount")).text

    countLIST = countListbefore.split(' ')

    beforeCount = countLIST[4]

    print("before count-->" + str(beforeCount))

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

    countListafter = driver.find_element(By.XPATH, baseMaster.get("UnitOfMeasurement", "unitCount")).text

    aftercountLIS = countListafter.split(' ')

    afterCount = aftercountLIS[4]

    print("afterCount-->" + afterCount)

    if afterCount==beforeCount-1:
        print("Unit Delete is working properly")
    
    else:
        print("Unit Delete is not working properly, Data is not deleted")


def unitEdit(driver,oldName,oldDescription,oldDefaultStatus,newName,newDescription):
    ScreenNavigate.unit(driver)

    countListbefore = driver.find_element(By.XPATH, baseMaster.get("UnitOfMeasurement", "unitCount")).text

    countLIST = countListbefore.split(' ')

    beforeCount = countLIST[4]

    print("before count-->" + str(beforeCount))

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
    countListafter = driver.find_element(By.XPATH, baseMaster.get("UnitOfMeasurement", "unitCount")).text

    aftercountLIS = countListafter.split(' ')

    afterCount = aftercountLIS[4]

    print("afterCount-->" + afterCount)

    if beforeCount == afterCount:
        print("New data is not created")
        print("Edit is working properly to the count")
    elif afterCount > beforeCount:
        print("New data is created for the edit action")

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







def auditTrailUnitAdd(driver,name,description,defaultStatus):

    ResultCase1="Unexecuted"

    beforeCount=TestCoverageAudittrail.auditTrailRecordCount(driver)

    print("once the count get")
    print(beforeCount)

    auditTrailRecord={"AuditAction":"ADD UNIT","comments":"Unit Name: {};Description: {};Default Status: No;".format(name,description),"userName":"Carl Dolman","userRole":"Admin","ActionType":"SYSTEM","ModuleName":"Base Master","FormName":"Unit of Measurement","esignComments":""}


    expectedAuditAction= auditTrailRecord.get("AuditAction")

    expectedComments=auditTrailRecord.get("comments")

    expectedUserName=auditTrailRecord.get("userName")

    expectedUserRole=auditTrailRecord.get("userRole")

    expectedActionType = auditTrailRecord.get("ActionType")

    expectedModuleName  = auditTrailRecord.get("ModuleName")

    expectedFormName = auditTrailRecord.get("FormName")

    expectedEsignComments = auditTrailRecord.get("esignComments")

    unitAdd(driver,name,description,"No")

    afterCount=TestCoverageAudittrail.auditTrailRecordCount(driver)

    auditActionList=driver.find_elements(By.XPATH, "//tbody[@role='presentation']/tr/td[2]")



    if afterCount==beforeCount:
        ResultCase1="FAIL"

        print("Audit trail is not captured")

    elif afterCount==beforeCount+1:

        i=2

        ResultCase1 = "PASS"

        print("Audit trail is captured")

        actualAuditDateAndTime=driver.find_element(By.XPATH,"//tbody[@role='presentation']/tr[2]/td[2]").text

        actualAuditAction=ElementAuditTrail.auditAction(driver,i).text



        if actualAuditAction==expectedAuditAction:
            print("Audit action is properly mentioned")

        else:
            print("Audit action is not properly mentioned")

        actualComments = ElementAuditTrail.auditComment(driver,i).text

        if actualComments==expectedComments:
            print("Comment is properly displayed")

        else:
            print("Comment is not displaying properly")


        actualUserName = ElementAuditTrail.userName(driver,i).text



        if actualUserName==expectedUserName:
            print("user name is properly displayed")

        else:
            print("user name is not displaying properly")


        actualUserRole = ElementAuditTrail.userRole(driver,i).text



        if actualUserRole == expectedUserRole:
            print("user role is properly displayed")

        else:
            print("user role is not displaying properly")

        actualActionType = ElementAuditTrail.actionType(driver,i).text


        if actualActionType == expectedActionType:
            print("Action type is properly displayed")

        else:
            print("Action type is not displaying properly")


        actualModuleName = ElementAuditTrail.moduleName(driver,i).text

        if expectedModuleName == actualModuleName:
            print("Module name  is properly displayed")

        else:
            print("Module name   is not displaying properly")

        actualFormName = ElementAuditTrail.formName(driver, i).text

        if actualFormName == expectedFormName:
            print("Form name is properly displayed")

        else:
            print("Form name is not displaying properly")

        actualEsignComments = ElementAuditTrail.esignComments(driver, i).text


        if actualEsignComments == expectedEsignComments:
            print("Esign comment is properly displayed")

        else:
            print("AEsign comment  is not displaying properly")

    elif afterCount>beforeCount+1:
        for i in range(0, afterCount - beforeCount):
            auditAction = auditActionList[i].text

            if auditAction == "UNIT ADD":

                userRole = ElementAuditTrail.userRole(driver, i).text

                i = i+2

                ResultCase1 = "PASS"

                print("Audit trail is captured")

                actualAuditDateAndTime = driver.find_element(By.XPATH, "//tbody[@role='presentation']/tr[2]/td[2]").text

                actualAuditAction = ElementAuditTrail.auditAction(driver, i).text

                if actualAuditAction == expectedAuditAction:
                    print("Audit action is properly mentioned")

                else:
                    print("Audit action is not properly mentioned")

                actualComments = ElementAuditTrail.auditComment(driver, i).text

                if actualComments == expectedComments:
                    print("Comment is properly displayed")

                else:
                    print("Comment is not displaying properly")

                actualUserName = ElementAuditTrail.userName(driver, i).text

                if actualUserName == expectedUserName:
                    print("user name is properly displayed")

                else:
                    print("user name is not displaying properly")

                actualUserRole = ElementAuditTrail.userRole(driver, i).text

                if actualUserRole == expectedUserRole:
                    print("user role is properly displayed")

                else:
                    print("user role is not displaying properly")

                actualActionType = ElementAuditTrail.actionType(driver, i).text

                if actualActionType == expectedActionType:
                    print("Action type is properly displayed")

                else:
                    print("Action type is not displaying properly")

                actualModuleName = ElementAuditTrail.moduleName(driver, i).text

                if expectedModuleName == actualModuleName:
                    print("Module name  is properly displayed")

                else:
                    print("Module name   is not displaying properly")

                actualFormName = ElementAuditTrail.formName(driver, i).text

                if actualFormName == expectedFormName:
                    print("Form name is properly displayed")

                else:
                    print("Form name is not displaying properly")

                actualEsignComments = ElementAuditTrail.esignComments(driver, i).text

                if actualEsignComments == expectedEsignComments:
                    print("Esign comment is properly displayed")

                else:
                    print("Esign comment  is not displaying properly")


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

    unitNameFilter = driver.find_element(By.XPATH, "(//span[@role='listbox'])[2]")

    unitNameFilter.click()

    driver.find_element(By.XPATH,"//*[text()='Is equal to']").click()

    textA=" (//input[@class='k-textbox'])[1]"

    clear="//button[@class='k-button' and text()='Clear']"

    filter="//button[@class='k-button k-primary' and text()='Filter']"

    name="cm"
    BasicOperation.sendKeysXpath(driver,textA,name)

    BasicOperation.clickXpath(driver,filter)

    rowList = driver.find_elements(By.TAG_NAME, "tr")

    for i in rowList:
        rowText=i.text

        if rowText.__contains__(name):
            print("data shows properly")











#driver=BrowserOperation.launchLIMS()

#unitFilter(driver)





def auditTrailUnitEdit(driver,oldName,oldDescription,newName,newDescription,defaultStatus):

    ResultCase1="Unexecuted"

    beforeCount=TestCoverageAudittrail.auditTrailRecordCount(driver)

    print("once the count get")
    
    print(beforeCount)

    auditTrailRecord={"AuditAction":"EDIT UNIT","comments":"Unit Name: {}-> {};Description: {}-> ;	".format(oldName,newName,oldDescription),"userName":"Carl Dolman","userRole":"Admin","ActionType":"SYSTEM","ModuleName":"Base Master","FormName":"Unit of Measurement","esignComments":""}

    unitEdit(driver,oldName,oldDescription,"No",newName,newDescription)

    BrowserOperation.refreshLogin(driver)

    expectedAuditAction = auditTrailRecord.get("AuditAction")

    expectedComments = auditTrailRecord.get("comments")

    expectedUserName = auditTrailRecord.get("userName")

    expectedUserRole = auditTrailRecord.get("userRole")

    expectedActionType = auditTrailRecord.get("ActionType")

    expectedModuleName = auditTrailRecord.get("ModuleName")

    expectedFormName = auditTrailRecord.get("FormName")

    expectedEsignComments = auditTrailRecord.get("esignComments")



    afterCount = TestCoverageAudittrail.auditTrailRecordCount(driver)

    auditActionList = driver.find_elements(By.XPATH, "//tbody[@role='presentation']/tr/td[2]")

    if afterCount == beforeCount:
        ResultCase1 = "FAIL"

        print("Audit trail is not captured")

    elif afterCount == beforeCount + 1:

        i = 2

        ResultCase1 = "PASS"

        print("Audit trail is captured")

        actualAuditDateAndTime = driver.find_element(By.XPATH, "//tbody[@role='presentation']/tr[2]/td[2]").text

        actualAuditAction = ElementAuditTrail.auditAction(driver, i).text

        print("actualAuditAction "+actualAuditAction)
        print("expectedAuditAction "+expectedAuditAction)

        if actualAuditAction == expectedAuditAction:
            print("Audit action is properly mentioned")

        else:
            print("Audit action is not properly mentioned")

        actualComments = ElementAuditTrail.auditComment(driver, i).text


        print("actualComments "+actualComments)
        print("expectedComments "+expectedComments)

        if actualComments == expectedComments:
            print("Comment is properly displayed")

        else:
            print("Comment is not displaying properly")

        actualUserName = ElementAuditTrail.userName(driver, i).text


        print("actualUserName "+actualUserName)
        print("expectedUserName "+expectedUserName)

        if actualUserName == expectedUserName:
            print("user name is properly displayed")

        else:
            print("user name is not displaying properly")

        actualUserRole = ElementAuditTrail.userRole(driver, i).text


        print("actualUserRole "+actualUserRole)
        print("expectedUserRole "+expectedUserRole)

        if actualUserRole == expectedUserRole:
            print("user role is properly displayed")

        else:
            print("user role is not displaying properly")

        actualActionType = ElementAuditTrail.actionType(driver, i).text


        print("actualActionType "+actualActionType)
        print("expectedActionType "+expectedActionType)

        if actualActionType == expectedActionType:
            print("Action type is properly displayed")

        else:
            print("Action type is not displaying properly")

        actualModuleName = ElementAuditTrail.moduleName(driver, i).text



        print("actualModuleName "+actualModuleName)
        print("expectedModuleName "+expectedModuleName)


        if expectedModuleName == actualModuleName:
            print("Module name  is properly displayed")

        else:
            print("Module name   is not displaying properly")

        actualFormName = ElementAuditTrail.formName(driver, i).text


        print("actualFormName "+actualFormName)
        print("expectedFormName "+expectedFormName)

        if actualFormName == expectedFormName:
            print("Form name is properly displayed")

        else:
            print("Form name is not displaying properly")

        actualEsignComments = ElementAuditTrail.esignComments(driver, i).text


        print("actualEsignComments "+actualEsignComments)
        print("expectedEsignComments "+expectedEsignComments)


        if actualEsignComments == expectedEsignComments:
            print("Esign comment is properly displayed")

        else:
            print("AEsign comment  is not displaying properly")

    elif afterCount > beforeCount + 1:
         for i in range(0, afterCount - beforeCount):
                 auditAction = auditActionList[i].text

                 if auditAction == "UNIT ADD":

                    userRole = ElementAuditTrail.userRole(driver, i).text

                    i = i + 2

                    ResultCase1 = "PASS"

                    print("Audit trail is captured")

                    actualAuditDateAndTime = driver.find_element(By.XPATH, "//tbody[@role='presentation']/tr[2]/td[2]").text

                    actualAuditAction = ElementAuditTrail.auditAction(driver, i).text

                    print("actualAuditAction " + actualAuditAction)
                    print("expectedAuditAction " + expectedAuditAction)

                    if actualAuditAction == expectedAuditAction:
                        print("Audit action is properly mentioned")

                    else:
                        print("Audit action is not properly mentioned")

                    actualComments = ElementAuditTrail.auditComment(driver, i).text


                    print("actualComments " + actualComments)
                    print("expectedComments " + expectedComments)

                    if actualComments == expectedComments:
                            print("Comment is properly displayed")

                    else:
                            print("Comment is not displaying properly")

                    actualUserName = ElementAuditTrail.userName(driver, i).text

                    if actualUserName == expectedUserName:
                            print("user name is properly displayed")

                    else:
                            print("user name is not displaying properly")

                    actualUserRole = ElementAuditTrail.userRole(driver, i).text

                    if actualUserRole == expectedUserRole:
                            print("user role is properly displayed")

                    else:
                            print("user role is not displaying properly")
                    actualActionType = ElementAuditTrail.actionType(driver, i).text

                    if actualActionType == expectedActionType:
                        print("Action type is properly displayed")

                    else:
                         print("Action type is not displaying properly")

                    actualModuleName = ElementAuditTrail.moduleName(driver, i).text

                    if expectedModuleName == actualModuleName:
                        print("Module name  is properly displayed")

                    else:
                        print("Module name   is not displaying properly")

                    actualFormName = ElementAuditTrail.formName(driver, i).text

                    if actualFormName == expectedFormName:
                        print("Form name is properly displayed")

                    else:
                        print("Form name is not displaying properly")

                    actualEsignComments = ElementAuditTrail.esignComments(driver, i).text

                    if actualEsignComments == expectedEsignComments:
                        print("Esign comment is properly displayed")

                    else:
                        print("Esign comment  is not displaying properly")




def auditTrailUnitDelete(driver,name,description,defaultStatus):

    ResultCase1="Unexecuted"

    beforeCount=TestCoverageAudittrail.auditTrailRecordCount(driver)

    print("once the count get")
    print(beforeCount)

    auditTrailRecord={"AuditAction":"DELETE UNIT","comments":"Unit Name: {};Description: {};Default Status: No;	".format(name,description),"userName":"Carl Dolman","userRole":"Admin","ActionType":"SYSTEM","ModuleName":"Base Master","FormName":"Unit of Measurement","esignComments":""}

    unitDelete(driver,name,description,"No")

    BrowserOperation.refreshLogin(driver)

    expectedAuditAction = auditTrailRecord.get("AuditAction")

    expectedComments = auditTrailRecord.get("comments")

    expectedUserName = auditTrailRecord.get("userName")

    expectedUserRole = auditTrailRecord.get("userRole")

    expectedActionType = auditTrailRecord.get("ActionType")

    expectedModuleName = auditTrailRecord.get("ModuleName")

    expectedFormName = auditTrailRecord.get("FormName")

    expectedEsignComments = auditTrailRecord.get("esignComments")

    afterCount = TestCoverageAudittrail.auditTrailRecordCount(driver)

    auditActionList = driver.find_elements(By.XPATH, "//tbody[@role='presentation']/tr/td[2]")

    if afterCount == beforeCount:
        ResultCase1 = "FAIL"

        print("Audit trail is not captured")

    elif afterCount == beforeCount + 1:

        i = 2

        ResultCase1 = "PASS"

        print("Audit trail is captured")

        actualAuditDateAndTime = driver.find_element(By.XPATH, "//tbody[@role='presentation']/tr[2]/td[2]").text

        actualAuditAction = ElementAuditTrail.auditAction(driver, i).text

        if actualAuditAction == expectedAuditAction:
            print("Audit action is properly mentioned")

        else:
            print("Audit action is not properly mentioned")

        actualComments = ElementAuditTrail.auditComment(driver, i).text

        if actualComments == expectedComments:
            print("Comment is properly displayed")

        else:
            print("Comment is not displaying properly")

        actualUserName = ElementAuditTrail.userName(driver, i).text

        if actualUserName == expectedUserName:
            print("user name is properly displayed")

        else:
            print("user name is not displaying properly")

        actualUserRole = ElementAuditTrail.userRole(driver, i).text

        if actualUserRole == expectedUserRole:
            print("user role is properly displayed")

        else:
            print("user role is not displaying properly")

        actualActionType = ElementAuditTrail.actionType(driver, i).text

        if actualActionType == expectedActionType:
            print("Action type is properly displayed")

        else:
            print("Action type is not displaying properly")

        actualModuleName = ElementAuditTrail.moduleName(driver, i).text

        if expectedModuleName == actualModuleName:
            print("Module name  is properly displayed")

        else:
            print("Module name   is not displaying properly")

        actualFormName = ElementAuditTrail.formName(driver, i).text

        if actualFormName == expectedFormName:
            print("Form name is properly displayed")

        else:
            print("Form name is not displaying properly")

        actualEsignComments = ElementAuditTrail.esignComments(driver, i).text

        if actualEsignComments == expectedEsignComments:
            print("Esign comment is properly displayed")

        else:
            print("AEsign comment  is not displaying properly")

    elif afterCount > beforeCount + 1:
        for i in range(0, afterCount - beforeCount):
            auditAction = auditActionList[i].text

            if auditAction == "UNIT ADD":

                userRole = ElementAuditTrail.userRole(driver, i).text

                i = i + 2

                ResultCase1 = "PASS"

                print("Audit trail is captured")

                actualAuditDateAndTime = driver.find_element(By.XPATH, "//tbody[@role='presentation']/tr[2]/td[2]").text

                actualAuditAction = ElementAuditTrail.auditAction(driver, i).text

                if actualAuditAction == expectedAuditAction:
                    print("Audit action is properly mentioned")

                else:
                    print("Audit action is not properly mentioned")

                actualComments = ElementAuditTrail.auditComment(driver, i).text

                if actualComments == expectedComments:
                    print("Comment is properly displayed")

                else:
                    print("Comment is not displaying properly")

                    actualUserName = ElementAuditTrail.userName(driver, i).text

                if actualUserName == expectedUserName:
                    print("user name is properly displayed")

                else:
                    print("user name is not displaying properly")

                    actualUserRole = ElementAuditTrail.userRole(driver, i).text

                if actualUserRole == expectedUserRole:
                    print("user role is properly displayed")

                else:
                    print("user role is not displaying properly")
                actualActionType = ElementAuditTrail.actionType(driver, i).text

                if actualActionType == expectedActionType:
                    print("Action type is properly displayed")

                else:
                    print("Action type is not displaying properly")

                actualModuleName = ElementAuditTrail.moduleName(driver, i).text

                if expectedModuleName == actualModuleName:
                    print("Module name  is properly displayed")

                else:
                    print("Module name   is not displaying properly")

                actualFormName = ElementAuditTrail.formName(driver, i).text

                if actualFormName == expectedFormName:
                    print("Form name is properly displayed")

                else:
                    print("Form name is not displaying properly")

                actualEsignComments = ElementAuditTrail.esignComments(driver, i).text

                if actualEsignComments == expectedEsignComments:
                    print("Esign comment is properly displayed")

                else:
                    print("Esign comment  is not displaying properly")



