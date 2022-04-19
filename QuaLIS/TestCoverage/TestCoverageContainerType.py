import datetime
from os import listdir

import keyboard
import time
from configparser import ConfigParser

from selenium.webdriver.common.by import By

from ObjectRepository import ElementAuditTrail
from TestCoverage import TestCoverageAudittrail
from Utility import BasicOperation, ScreenNavigate, BrowserOperation, ResultFlag, LogOperation, ExceptionHandling, JDBC
from Utility.BrowserOperation import configDriver
from loguru import logger

section="Container Type"

baseMaster = ConfigParser()
baseMaster.read(BasicOperation.projectDirectory() + "\\ObjectRepository\\ElementBaseMaster.ini")


def containerTypeAdd(driver, name, description):


    ScreenNavigate.containerType(driver)


    try:
        countListbefore = driver.find_element(By.XPATH, baseMaster.get(section, "containerTypeCount")).text

        countLIST = countListbefore.split(' ')

        beforeCount = countLIST[4]

        logger.info("Checked the count before add the container type detail, The count in the text is " + beforeCount)

    except:

        try:

            time.sleep(3)
            countListbefore = driver.find_element(By.XPATH, baseMaster.get(section, "containerTypeCount")).text

            countLIST = countListbefore.split(' ')

            beforeCount = countLIST[4]

            logger.info(
                "Checked the count before add the container type detail, The count in the text is " + beforeCount)


        except:
            logger.error("Unable to get the count detail")

            beforeCount=None



    ExceptionHandling.exceptionClick(driver, baseMaster.get(section, "containerTypeAdd"), "Clicked the container type add button", "Unable to click the container type add button")

    ExceptionHandling.exceptionSendKeys(driver, baseMaster.get(section, "containerTypeName"), name,
                                        "Entered the container type name", "Unable to enter the container type name")

    ExceptionHandling.exceptionSendKeys(driver, baseMaster.get(section, "containerTypeDescription"), description,
                                        "Entered the container type description", "Unable to enter the container type description")

    ExceptionHandling.exceptionClick(driver,
                                     baseMaster.get(section, "containerTypeAddSubmit"),
                                     "Clicked the add submit button", "unable to click the add submit button")

    time.sleep(2)

    addTime = BasicOperation.timet()

    try:
        countListafter = driver.find_element(By.XPATH, baseMaster.get(section, "containerTypeCount")).text

        countLIST = countListafter.split(' ')

        afterCount = countLIST[4]

        logger.info("Checked the count after add the container type detail, The count in the text is " + afterCount)

    except:

        try:

            time.sleep(3)
            countListafter = driver.find_element(By.XPATH, baseMaster.get(section, "containerTypeCount")).text

            countLIST = countListafter.split(' ')

            afterCount = countLIST[4]

            logger.info(
                "Checked the count before add the container type detail, The count in the text is " + beforeCount)

        except:
            logger.error("Unable to get the count detail")
            afterCount=None


    if int(afterCount)==int(beforeCount)+1:
         result="unit added successfully"
         logger.info(result)

    elif int(afterCount)==int(beforeCount)==None:

         result = "Unable to get the count detail properly"
         logger.info(result)

    else:

         result = "Unit add is not working properly"
         logger.error(result)


    element = driver.find_element(By.XPATH, "//span[text()='Base Master']")
    time.sleep(2)
    try:
        driver.execute_script("arguments[0].scrollIntoView();", element)
    except:
        pass
    element.click()

    output = {"addtime": addTime}

    return output


def unitDelete(driver, name, description, defaultStatus):


    ScreenNavigate.containerType(driver)

    countListbefore = driver.find_element(By.XPATH, baseMaster.get(section, "containerTypeCount")).text

    countLIST = countListbefore.split(' ')

    beforeCount = int(countLIST[len(countLIST) - 1])

    print("before count-->" + str(beforeCount))

    q = driver.find_elements(By.TAG_NAME, "tr")
    qq = len(q)

    # input("enter containertype with description: ")
    unit = name + " " + description + " " + defaultStatus
    for i in range(1, qq):
        unitrow = q[i].text

        if unit.__contains__(name):
            print("unit delete Matched at " + str(i))
            print("unit count is", i, unitrow)
            print(i)
            m = str(i)
            delete = "(//span[@data-tip='Delete'])[" + m + "]"
            print(delete)
            driver.find_element(By.XPATH, delete).click()

            driver.find_element(By.XPATH, "//*[text()='OK']").click()

            break

        else:
            print("Not matched")

        element = driver.find_element(By.XPATH, "//span[text()='Base Master']")

        try:
            driver.execute_script("arguments[0].scrollIntoView();", element)
        except:
            pass

        element.click()

    time.sleep(2)

    countListafter = driver.find_element(By.XPATH, baseMaster.get("UnitOfMeasurement", "unitCount")).text

    aftercountLIS = countListafter.split(' ')

    afterCount = int(aftercountLIS[len(aftercountLIS) - 1])

    print("afterCount-->" + str(afterCount))

    if afterCount == beforeCount - 1:
        print("Unit Delete is working properly")
    else:
        print("Unit Delete is not working properly, Data is not deleted")


def unitEdit(driver, oldName, oldDescription, oldDefaultStatus, newName, newDescription):
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

        print("unitrow " + unitrow)

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

            BasicOperation.clear(driver, baseMaster.get("UnitOfMeasurement", "unitDescription"))

            BasicOperation.sendKeysXpath(driver, baseMaster.get("UnitOfMeasurement", "unitName"), newName)

            # BasicOperation.sendKeysXpath(driver, baseMaster.get("UnitOfMeasurement", "unitDescription"),
            # newDescription)

            BasicOperation.clickXpath(driver,
                                      baseMaster.get("UnitOfMeasurement", "unitEditSubmit"))

            break

        else:
            print("Not matched")

    time.sleep(2)

    countListafter = driver.find_element(By.XPATH, baseMaster.get("UnitOfMeasurement", "unitCount")).text

    print(countListafter)

    aftercountLIS = countListafter.split(' ')

    afterCount = aftercountLIS[len(aftercountLIS) - 1]

    print("afterCount-->" + afterCount)

    if beforeCount == afterCount:
        print("New data is not created")
        print("Edit is working properly to the count")
    elif afterCount > beforeCount:
        print("New data is created for the edit action")

    element = driver.find_element(By.XPATH, "//span[text()='Base Master']")

    try:
        driver.execute_script("arguments[0].scrollIntoView();", element)
    except:
        pass

    element.click()


def auditTrailUnitAdd(driver, name, description, defaultStatus):
    ResultCase1 = "Unexecuted"

    beforeCount = TestCoverageAudittrail.auditTrailRecordCount(driver)

    print("once the count get")
    print(beforeCount)

    userName = JDBC.userName()

    # output = unitAdd(driver, name, description, "No")

    configDriver = ConfigParser()
    configDriver.read(BasicOperation.projectDirectory() + "\\config.ini")

    userRole = configDriver.get("Credential", "userRole")

    auditTrailRecord = {"AuditDateAndTime": output.get("addtime"), "AuditAction": "ADD UNIT",
                        "comments": "Unit Name: {};Description: {};Default Status: No;".format(name, description),
                        "userName": "{}".format(userName), "userRole": "{}".format(userRole), "ActionType": "SYSTEM",
                        "ModuleName": "Base Master", "FormName": "Unit of Measurement", "esignComments": ""}

    expectedAuditAction = auditTrailRecord.get("AuditAction")

    expectedComments = auditTrailRecord.get("comments")

    expectedUserName = auditTrailRecord.get("userName")

    expectedUserRole = auditTrailRecord.get("userRole")

    expectedActionType = auditTrailRecord.get("ActionType")

    expectedModuleName = auditTrailRecord.get("ModuleName")

    expectedFormName = auditTrailRecord.get("FormName")

    expectedEsignComments = auditTrailRecord.get("esignComments")

    # expectedTime=auditTrailRecord.get("addtime")[0:15]

    time.sleep(3)

    afterCount = TestCoverageAudittrail.auditTrailRecordCount(driver)

    logger.info("After count is " + str(afterCount))

    auditActionList = driver.find_elements(By.XPATH, "//tbody[@role='presentation']/tr[2]/td[2]")

    if afterCount == beforeCount:
        ResultCase1 = "FAIL"

        result = "Audit trail is not captured"

        logger.error(result)


    elif afterCount == beforeCount + 1:

        i = 2

        ResultCase1 = "PASS"

        result = "Audit trail is captured"

        logger.info(result)

        # actualAuditDateAndTime=driver.find_element(By.XPATH,"//tbody[@role='presentation']/tr[2]/td[2]").text
        #
        # auditTime=actualAuditDateAndTime[0:15]
        #
        # if expectedTime.__contains__(auditTime):
        #     logger.info("Login time shows correctly")
        # else:
        #     logger.error("Time detail is not  shown correctly")

        actualAuditAction = driver.find_element(By.XPATH, "//tbody[@role='presentation']/tr[2]/td[3]").text

        if actualAuditAction == expectedAuditAction:
            logger.info("Audit action is properly mentioned")

        else:
            print("Audit action is not properly mentioned")

        actualComments = driver.find_element(By.XPATH, "//tbody[@role='presentation']/tr[2]/td[4]").text

        if actualComments == expectedComments:

            logger.info("Comment is properly displayed")

        else:
            print("Comment is not displaying properly")

        actualUserName = driver.find_element(By.XPATH, "//tbody[@role='presentation']/tr[2]/td[5]").text

        if actualUserName == expectedUserName:
            result = "user name is properly displayed"

            logger.info(result)

        actualUserRole = driver.find_element(By.XPATH, "//tbody[@role='presentation']/tr[2]/td[6]").text

        if actualUserRole == expectedUserRole:

            result = "user role is properly displayed"

            logger.info(result)

        else:
            result = "user role is not displaying properly"
            logger.error(result)

        actualActionType = driver.find_element(By.XPATH, "//tbody[@role='presentation']/tr[2]/td[7]").text

        if actualActionType == expectedActionType:

            result = "Action type is properly displayed"

            logger.info(result)

        else:
            result = "Action type is not displaying properly"

            logger.error(result)

        actualModuleName = driver.find_element(By.XPATH, "//tbody[@role='presentation']/tr[2]/td[8]").text

        if expectedModuleName == actualModuleName:

            result = "Module name  is properly displayed"

            logger.info(result)


        else:

            result = "Module name   is not displaying properly"

            logger.error(result)

        actualFormName = driver.find_element(By.XPATH, "//tbody[@role='presentation']/tr[2]/td[9]").text

        if actualFormName == expectedFormName:

            result = "Form name is properly displayed"

            logger.info(result)

        else:
            print("Form name is not displaying properly")

        actualEsignComments = driver.find_element(By.XPATH, "//tbody[@role='presentation']/tr[2]/td[10]").text

        if actualEsignComments == expectedEsignComments:

            result = "Esign comment is properly displayed"

            logger.info(result)
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


def downloadPDF(driver):
    time.sleep(2)

    download = ConfigParser()
    download.read(BasicOperation.projectDirectory() + "\\config.ini")

    downloadPath = download.get("config", "download")

    onlyfiles = [f for f in listdir(downloadPath)]

    beforeCount = len(onlyfiles)

    beforeCountResult = "Number of folder and files before download " + str(beforeCount)

    logger.info(beforeCountResult)

    ScreenNavigate.containerType(driver)

    try:
        BasicOperation.clickXpath(driver, baseMaster.get(section, "containerTypeDownloadPDF"))
        result = "Clicked the Download PDF button"

        LogOperation.logInfo(result)

        logger.info(result)
    except Exception as e:

        result = "Unable to click the Download PDF button, It causes the exception, Exception Detail---> " + str(e)

        LogOperation.logError(result)

        logger.error(result)

    time.sleep(5)

    onlyfiles2 = [f for f in listdir(downloadPath)]

    afterCount = len(onlyfiles2)

    afterCountResult = "Number of folder and files after download " + str(afterCount)

    logger.info(afterCountResult)

    if afterCount == beforeCount + 1:
        logger.info("File is downloaded")

    elif afterCount == beforeCount:
        logger.error("File is not downloaded")

    else:
        logger.error("File is not downloaded properly")

    try:
        element = driver.find_element(By.XPATH, "//span[text()='Base Master']")

        try:
            driver.execute_script("arguments[0].scrollIntoView();", element)
        except:
            pass

        element.click()

        result = "Clicked the basemaster icon"

        LogOperation.logInfo(result)

        logger.info(result)

    except Exception as e:

        result = "Unable to click the basemaster icon -- post condition, It causes exception-->" + str(e)
        LogOperation.logError(result)

        logger.error(result)


def downloadExcel(driver):

    download = ConfigParser()

    download.read(BasicOperation.projectDirectory() + "\\config.ini")

    downloadPath = download.get("config", "download")

    onlyfiles = [f for f in listdir(downloadPath)]

    beforeCount = len(onlyfiles)

    beforeCountResult = "Number of folder and files before download " + str(beforeCount)

    logger.info(beforeCountResult)

    ScreenNavigate.containerType(driver)

    time.sleep(1)

    try:
        BasicOperation.clickXpath(driver, baseMaster.get(section, "containerTypeDownloadExcel"))

        Result = "Clicked the Download Excel button"

        LogOperation.logInfo(Result)

        logger.info(Result)


    except Exception as e:
        result = "Unable to click the Download excel button, It causes the exception, Exception Detail---> " + str(e)
        LogOperation.logError(result)
        logger.error(result)

    time.sleep(5)

    onlyfiles2 = [f for f in listdir(downloadPath)]

    afterCount = len(onlyfiles2)

    afterCountResult = "Number of folder and files after download " + str(afterCount)

    logger.info(afterCountResult)

    if afterCount == beforeCount + 1:
        logger.info("File is downloaded")

        onlyfiles2 = [f for f in listdir(downloadPath)]

        missing = None

        for i in onlyfiles2:
            for j in onlyfiles:
                if i == j:
                    pass
                else:
                    missing = i

    elif afterCount == beforeCount:
        logger.error("File is not downloaded")

    else:
        logger.error("File is not downloaded properly")

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

        result = "Clicked the basemaster icon"

        logger.info(result)

        LogOperation.logInfo(result)

    except Exception as e:

        result = "Unable to click the basemaster icon -- post condition, It causes exception-->" + str(e)

        logger.error(result)

        LogOperation.logError(result)

def unitFilter(driver):
    ScreenNavigate.unit(driver)

    BasicOperation.clickXpath(driver, baseMaster.get("UnitOfMeasurement", "unitNameFilter"))

    unitNameFilter = driver.find_element(By.XPATH, "(//span[@role='listbox'])[2]")

    unitNameFilter.click()

    driver.find_element(By.XPATH, "//*[text()='Is equal to']").click()

    textA = " (//input[@class='k-textbox'])[1]"

    clear = "//button[@class='k-button' and text()='Clear']"

    filter = "//button[@class='k-button k-primary' and text()='Filter']"

    name = "cm"
    BasicOperation.sendKeysXpath(driver, textA, name)

    BasicOperation.clickXpath(driver, filter)

    rowList = driver.find_elements(By.TAG_NAME, "tr")

    for i in rowList:
        rowText = i.text

        if rowText.__contains__(name):
            print("data shows properly")


def auditTrailUnitEdit(driver, oldName, oldDescription, newName, newDescription, defaultStatus):
    ResultCase1 = "Unexecuted"

    beforeCount = TestCoverageAudittrail.auditTrailRecordCount(driver)

    print("once the count get")

    print(beforeCount)

    auditTrailRecord = {"AuditAction": "EDIT UNIT",
                        "comments": "Unit Name: {}-> {};Description: {}-> ;	".format(oldName, newName,
                                                                                        oldDescription),
                        "userName": "Carl Dolman", "userRole": "Admin", "ActionType": "SYSTEM",
                        "ModuleName": "Base Master", "FormName": "Unit of Measurement", "esignComments": ""}

    unitEdit(driver, oldName, oldDescription, "No", newName, newDescription)

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

        print("actualUserName " + actualUserName)
        print("expectedUserName " + expectedUserName)

        if actualUserName == expectedUserName:
            print("user name is properly displayed")

        else:
            print("user name is not displaying properly")

        actualUserRole = ElementAuditTrail.userRole(driver, i).text

        print("actualUserRole " + actualUserRole)
        print("expectedUserRole " + expectedUserRole)

        if actualUserRole == expectedUserRole:
            print("user role is properly displayed")

        else:
            print("user role is not displaying properly")

        actualActionType = ElementAuditTrail.actionType(driver, i).text

        print("actualActionType " + actualActionType)
        print("expectedActionType " + expectedActionType)

        if actualActionType == expectedActionType:
            print("Action type is properly displayed")

        else:
            print("Action type is not displaying properly")

        actualModuleName = ElementAuditTrail.moduleName(driver, i).text

        print("actualModuleName " + actualModuleName)
        print("expectedModuleName " + expectedModuleName)

        if expectedModuleName == actualModuleName:
            print("Module name  is properly displayed")

        else:
            print("Module name   is not displaying properly")

        actualFormName = ElementAuditTrail.formName(driver, i).text

        print("actualFormName " + actualFormName)
        print("expectedFormName " + expectedFormName)

        if actualFormName == expectedFormName:
            print("Form name is properly displayed")

        else:
            print("Form name is not displaying properly")

        actualEsignComments = ElementAuditTrail.esignComments(driver, i).text

        print("actualEsignComments " + actualEsignComments)
        print("expectedEsignComments " + expectedEsignComments)

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


def auditTrailUnitDelete(driver, name, description, defaultStatus):
    ResultCase1 = "Unexecuted"

    beforeCount = TestCoverageAudittrail.auditTrailRecordCount(driver)

    print("once the count get")
    print(beforeCount)

    auditTrailRecord = {"AuditAction": "DELETE UNIT",
                        "comments": "Unit Name: {};Description: {};Default Status: No;	".format(name, description),
                        "userName": "Carl Dolman", "userRole": "Admin", "ActionType": "SYSTEM",
                        "ModuleName": "Base Master", "FormName": "Unit of Measurement", "esignComments": ""}

    unitDelete(driver, name, description, "No")

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


def containerTypeEdit(driver, oldName, oldDescription, oldDefaultStatus, newName, newDescription):

    ScreenNavigate.containerType(driver)

    try:
        countListbefore = driver.find_element(By.XPATH, baseMaster.get(section, "containerTypeCount")).text

        countLIST = countListbefore.split(' ')

        beforeCount = countLIST[4]

        logger.info("Checked the count before edit container type detail, The count in the text is  " + beforeCount)

    except:

        try:

            time.sleep(3)

            countListbefore = driver.find_element(By.XPATH, baseMaster.get(section, "containerTypeCount")).text

            countLIST = countListbefore.split(' ')

            beforeCount = countLIST[4]

            logger.info(
                "Checked the count before edit the container type detail, The count in the text is " + beforeCount)
        except:
            logger.error("Unable to get the count detail")

            beforeCount = None

    rows = driver.find_elements(By.TAG_NAME, "tr")

    m=1

    for i in range(1,len(rows)):
        unitrow = rows[i].text

        if unitrow.__contains__(oldName):

            result="The data is matched at "+str(m)+" index"

            logger.info(result)

            edit = "(//span[@data-tip='Edit'])[" + str(m) + "]"

            driver.find_element(By.XPATH, edit).click()

            BasicOperation.clear(driver, baseMaster.get(section, "containerTypeDescription"))

            BasicOperation.clear(driver, baseMaster.get(section, "containerTypeName"))

            BasicOperation.clear(driver, baseMaster.get(section, "containerTypeDescription"))

            BasicOperation.sendKeysXpath(driver, baseMaster.get(section, "containerTypeName"), newName)

            # BasicOperation.sendKeysXpath(driver, baseMaster.get("UnitOfMeasurement", "unitDescription"),
            # newDescription)

            BasicOperation.clickXpath(driver,
                                      baseMaster.get(section, "containerTypeEditSubmit"))

            break

        else:
            logger.error("The data is not available in the grid")

        m=m+1

    time.sleep(2)

    try:
        countListAfter = driver.find_element(By.XPATH, baseMaster.get(section, "containerTypeCount")).text

        countLIST = countListAfter.split(' ')

        afterCount = countLIST[4]

        logger.info("Checked the count after edit  container type detail, The count in the text is  " + afterCount)

    except:

        try:

            time.sleep(3)
            countListAfter = driver.find_element(By.XPATH, baseMaster.get(section, "containerTypeCount")).text

            countLIST = countListAfter.split(' ')

            afterCount = countLIST[4]

            logger.info(
                "Checked the count after edit  container type detail, The count in the text is  " + afterCount)

        except:
            logger.error("Unable to get the count detail")

            afterCount = None

    if beforeCount == afterCount:
        print("New data is not created")
        print("Edit is working properly to the count")
    elif afterCount > beforeCount:
        print("New data is created for the edit action")

    element = driver.find_element(By.XPATH, "//span[text()='Base Master']")

    try:
        driver.execute_script("arguments[0].scrollIntoView();", element)
    except:
        pass
    element.click()



def containerTypeDelete(driver, name, description, defaultStatus):

    ScreenNavigate.containerType(driver)

    try:
        countListbefore = driver.find_element(By.XPATH, baseMaster.get(section, "containerTypeCount")).text

        countLIST = countListbefore.split(' ')

        beforeCount = countLIST[4]

        logger.info("Checked the count before delete the container Type detail, The count in the text is  " + beforeCount)

    except:

        try:

            time.sleep(3)
            countListbefore = driver.find_element(By.XPATH, baseMaster.get(section, "containerTypeCount")).text

            countLIST = countListbefore.split(' ')

            beforeCount = countLIST[4]

            logger.info(
                "Checked the count before edit the container type detail, The count in the text is " + beforeCount)
        except:
            logger.error("Unable to get the count detail")

            beforeCount = None

    rows = driver.find_elements(By.TAG_NAME, "tr")


    m=1

    for i in range(1,len(rows)):
        unitrow = rows[i].text

        if unitrow.__contains__(name):

            result="The data is matched at "+str(m)+" index"

            logger.info(result)

            delete = "(//span[@data-tip='Delete'])[" + str(m) + "]"

            driver.find_element(By.XPATH, delete).click()

            driver.find_element(By.XPATH, "//*[text()='OK']").click()

            break

        else:
            logger.error("The data is not available in the grid")

        m=m+1

    time.sleep(2)

    try:
        countListAfter = driver.find_element(By.XPATH, baseMaster.get(section, "containerTypeCount")).text

        countLIST = countListAfter.split(' ')

        afterCount = countLIST[4]

        logger.info("Checked the count after delete the container Type detail, The count in the text is  " + afterCount)

    except:

        try:

            time.sleep(3)
            countListAfter = driver.find_element(By.XPATH, baseMaster.get(section, "containerTypeCount")).text

            countLIST = countListAfter.split(' ')

            afterCount = countLIST[4]

            logger.info(
                "Checked the count after delete the  container Type detail, The count in the text is  " + afterCount)

        except:
            logger.error("Unable to get the count detail")

            afterCount = None


    element = driver.find_element(By.XPATH, "//span[text()='Base Master']")

    try:
            driver.execute_script("arguments[0].scrollIntoView();", element)
    except:
            pass

    element.click()
