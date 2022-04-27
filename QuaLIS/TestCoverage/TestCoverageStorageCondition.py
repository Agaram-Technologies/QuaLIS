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

baseMaster = ConfigParser()
baseMaster.read(BasicOperation.projectDirectory() + "\\ObjectRepository\\ElementBaseMaster.ini")

section="Storage Condition"
def storageConditionAdd(driver, name, description,defaultStatus):

    ScreenNavigate.storageCondition(driver)

    try:
        countListbefore = driver.find_element(By.XPATH, baseMaster.get(section, "storageConditionCount")).text

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



    ExceptionHandling.exceptionClick(driver, baseMaster.get(section, "storageConditionAdd"), "Clicked the storage Condition add button", "Unable to click the storage Condition add button")

    ExceptionHandling.exceptionSendKeys(driver, baseMaster.get(section, "storageConditionName"), name,
                                        "Entered the storage Condition name", "Unable to enter the storage Condition name")
    ExceptionHandling.exceptionSendKeys(driver, baseMaster.get(section, "storageConditionDescription"), description,
                                        "Entered the storage Condition description", "Unable to enter the storage Condition description")

    ExceptionHandling.exceptionClick(driver,
                                     baseMaster.get(section, "storageConditionAddSubmit"),
                                     "Clicked the add submit button", "unable to click the add submit button")

    time.sleep(2)

    addTime = BasicOperation.timet()

    try:
        countListafter = driver.find_element(By.XPATH, baseMaster.get(section, "storageConditionCount")).text

        countLIST = countListafter.split(' ')

        afterCount = countLIST[4]

        logger.info("Checked the count after add the  detail, The count in the text is " + afterCount)

    except:

        try:

            time.sleep(3)
            countListafter = driver.find_element(By.XPATH, baseMaster.get(section, "storageConditionCount")).text

            countLIST = countListafter.split(' ')

            afterCount = countLIST[4]

            logger.info(
                "Checked the count before add the storageCondition detail, The count in the text is " + beforeCount)

        except:
            logger.error("Unable to get the count detail")
            afterCount=None


    if int(afterCount)==int(beforeCount)+1:
         result="storage Condition added successfully"
         logger.info(result)

    elif int(afterCount)==int(beforeCount)==None:

         result = "Unable to get the count detail properly"
         logger.info(result)

    else:

         result = "storage Condition add is not working properly"
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


def storageConditionDelete(driver, name, description, defaultStatus):

    ScreenNavigate.storageCondition(driver)

    try:
        countListbefore = driver.find_element(By.XPATH, baseMaster.get(section, "storageConditionCount")).text

        countLIST = countListbefore.split(' ')

        beforeCount = countLIST[4]

        logger.info("Checked the count before delete the storage condition detail, The count in the text is  " + beforeCount)

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
        countListAfter = driver.find_element(By.XPATH, baseMaster.get(section, "storageConditionCount")).text

        countLIST = countListAfter.split(' ')

        afterCount = countLIST[4]

        logger.info("Checked the count after delete the storage condition detail, The count in the text is  " + afterCount)

    except:

        try:

            time.sleep(3)
            countListAfter = driver.find_element(By.XPATH, baseMaster.get(section, "storageConditionCount")).text

            countLIST = countListAfter.split(' ')

            afterCount = countLIST[4]

            logger.info(
                "Checked the count after delete the  storage condition detail, The count in the text is  " + afterCount)

        except:
            logger.error("Unable to get the count detail")

            afterCount = None


    element = driver.find_element(By.XPATH, "//span[text()='Base Master']")

    try:
            driver.execute_script("arguments[0].scrollIntoView();", element)
    except:
            pass

    element.click()

    countListafter = driver.find_element(By.XPATH, baseMaster.get("UnitOfMeasurement", "unitCount")).text

    aftercountLIS = countListafter.split(' ')

    afterCount = int(aftercountLIS[len(aftercountLIS) - 1])

    print("afterCount-->" + str(afterCount))

    if afterCount == int(beforeCount) - 1:
        print("Unit Delete is working properly")
    else:
        print("Unit Delete is not working properly, Data is not deleted")


def storageConditionEdit(driver, oldName, oldDescription, oldDefaultStatus, newName, newDescription):


    ScreenNavigate.storageCondition(driver)

    try:
        countListbefore = driver.find_element(By.XPATH, baseMaster.get(section, "storageConditionCount")).text

        countLIST = countListbefore.split(' ')

        beforeCount = countLIST[4]

        logger.info("Checked the count before edit  storage condition detail, The count in the text is  " + beforeCount)

    except:

        try:

            time.sleep(3)
            countListbefore = driver.find_element(By.XPATH, baseMaster.get(section, "storageConditionCount")).text

            countLIST = countListbefore.split(' ')

            beforeCount = countLIST[4]

            logger.info(
                "Checked the count before edit the storage condition detail, The count in the text is " + beforeCount)
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

            BasicOperation.clear(driver, baseMaster.get(section, "storageConditionDescription"))

            BasicOperation.clear(driver, baseMaster.get(section, "storageConditionName"))

            BasicOperation.clear(driver, baseMaster.get(section, "storageConditionDescription"))

            BasicOperation.sendKeysXpath(driver, baseMaster.get(section, "storageConditionName"), newName)

            # BasicOperation.sendKeysXpath(driver, baseMaster.get("UnitOfMeasurement", "unitDescription"),
            # newDescription)

            BasicOperation.clickXpath(driver,
                                      baseMaster.get(section, "storageConditionEditSubmit"))

            break

        else:
            logger.error("The data is not available in the grid")

        m=m+1

    time.sleep(2)

    try:
        countListAfter = driver.find_element(By.XPATH, baseMaster.get(section, "storageConditionCount")).text

        countLIST = countListAfter.split(' ')

        afterCount = countLIST[4]

        logger.info("Checked the count after edit  storage condition detail, The count in the text is  " + afterCount)

    except:

        try:

            time.sleep(3)
            countListAfter = driver.find_element(By.XPATH, baseMaster.get(section, "storageConditionCount")).text

            countLIST = countListAfter.split(' ')

            afterCount = countLIST[4]

            logger.info(
                "Checked the count after edit  storage condition detail, The count in the text is  " + afterCount)

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


def auditTrailtorageConditionAdd(driver, name, description, defaultStatus):
    ResultCase1 = "Unexecuted"

    beforeCount = TestCoverageAudittrail.auditTrailRecordCount(driver)

    print("once the count get")
    print(beforeCount)

    userName = JDBC.userName()

    output = storageConditionAdd(driver, name, description, "No")

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

    ScreenNavigate.storageCondition(driver)

    try:
        BasicOperation.clickXpath(driver, baseMaster.get(section, "storageConditionDownloadPDF"))
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

    ScreenNavigate.storageCondition(driver)

    time.sleep(1)

    try:
        BasicOperation.clickXpath(driver, baseMaster.get(section, "storageConditionDownloadExcel"))

        Result = "Clicked the Download Excel button"

        LogOperation.logInfo(Result)

        logger.info(Result)



    except Exception as e:
        result = "Unable to click the Download excel button, It causes the exception, Exception Detail---> " + str(e)
        LogOperation.logError(result)
        logger.error(result)
        time.sleep(2)

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

    storageConditionEdit(driver, oldName, oldDescription, "No", newName, newDescription)

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

    storageConditionDelete(driver, name, description, "No")

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



def auditTrail(driver,expectedAuditTrailResult):

    expectedAuditAction=expectedAuditTrailResult.get("expectedAuditAction")


    expectedEsignComments=expectedAuditTrailResult.get("expectedEsignComments")

    expectedFormName = expectedAuditTrailResult.get("expectedFormName")


    expectedModuleName = expectedAuditTrailResult.get("expectedModuleName")


    expectedActionType = expectedAuditTrailResult.get("expectedActionType")


    expectedUserRole = expectedAuditTrailResult.get("expectedUserRole")



    expectedUserName = expectedAuditTrailResult.get("expectedUserName")


    expectedComments = expectedAuditTrailResult.get("expectedComments")



    actualAuditActionUI = driver.find_element(By.XPATH, "//tbody[@role='presentation']/tr[2]/td[3]").text

    if actualAuditActionUI == expectedAuditAction:

        logger.info("Audit action is properly mentioned in UI")
        logger.info("Expected--->" + expectedAuditAction)
        logger.info("Actual  --->" + actualAuditActionUI)

    else:
        logger.error("Audit action is not properly mentioned in UI")
        logger.error("Expected--->" + expectedAuditAction)
        logger.error("Actual  --->" + actualAuditActionUI)

    actualAuditActionDB = JDBC.retunOneValue(
        "select sauditaction from auditaction where nauditcode=(select COUNT(*) from auditaction )")

    if actualAuditActionDB == expectedAuditAction:

        logger.info("Audit action is properly mentioned in db")
        logger.info("Expected--->" + expectedAuditAction)
        logger.info("Actual  --->" + actualAuditActionDB)
    else:
        logger.error("Audit action is not properly mentioned db")
        logger.error("Expected--->" + expectedAuditAction)
        logger.error("Actual  --->" + actualAuditActionDB)

    if actualAuditActionUI == actualAuditActionDB:
        logger.info("Audit action is same in the db and ui")
        logger.info("actualAuditActionUI--->" + actualAuditActionUI)
        logger.info("actualAuditActionDB  --->" + actualAuditActionDB)
    else:
        logger.error("Audit action is not same in the db and ui")
        logger.error("actualAuditActionUI--->" + actualAuditActionUI)
        logger.error("actualAuditActionDB  --->" + actualAuditActionDB)

    actualCommentsUI = driver.find_element(By.XPATH, "//tbody[@role='presentation']/tr[2]/td[4]").text

    if actualCommentsUI == expectedComments:
        logger.info("Audit comment is properly mentioned in UI")
        logger.info("Expected--->" + expectedComments)
        logger.info("Actual  --->" + actualCommentsUI)
    else:
        logger.error("Audit comment is not properly mentioned in UI")
        logger.error("Expected--->" + expectedComments)
        logger.error("Actual  --->" + actualCommentsUI)

    actualCommentDb = JDBC.retunOneValue(
        "select scomments from auditcomments where nauditcode=(select COUNT(*)from auditaction)")

    if actualCommentDb == expectedComments:

        logger.info("Audit comment is properly mentioned in db")
        logger.info("Expected--->" + expectedComments)
        logger.info("Actual  --->" + actualCommentDb)
    else:
        logger.error("Audit action is not properly mentioned db")
        logger.error("Expected--->" + expectedComments)
        logger.error("Actual  --->" + actualCommentDb)

    if actualCommentsUI == actualCommentDb:
        logger.info("user role is same in the db and ui")
        logger.info("actualCommentsUI--->" + actualCommentsUI)
        logger.info("actualCommentDb  --->" + actualCommentDb)
    else:
        logger.error("user role is not same in the db and ui")
        logger.error("actualCommentsUI--->" + actualCommentsUI)
        logger.error("actualCommentDb  --->" + actualCommentDb)

    actualUserNameUI = driver.find_element(By.XPATH, "//tbody[@role='presentation']/tr[2]/td[5]").text

    if actualUserNameUI == expectedUserName:
        logger.info("user name is properly mentioned in UI")
        logger.info("Expected--->" + expectedUserName)
        logger.info("Actual  --->" + actualUserNameUI)
    else:
        logger.error("user name is not properly mentioned in UI")
        logger.error("Expected--->" + expectedUserName)
        logger.error("Actual  --->" + actualUserNameUI)

    actualUserRoleUI = driver.find_element(By.XPATH, "//tbody[@role='presentation']/tr[2]/td[6]").text

    if actualUserRoleUI == expectedUserRole:
        logger.info("user role is properly mentioned in UI")
        logger.info("Expected--->" + expectedUserRole)
        logger.info("Actual  --->" + actualUserRoleUI)

    else:
        logger.error("Audit action is not properly mentioned in UI")
        logger.error("Expected--->" + expectedUserRole)
        logger.error("Actual  --->" + actualUserRoleUI)

    queryr = "select suserrolename from userrole where nuserrolecode=(select nuserrole from auditaction where nauditcode=(select COUNT(*) from auditaction ))"

    actualUserRoleDB = JDBC.retunOneValue(queryr)

    if actualUserRoleDB == expectedUserRole:
        logger.info("user role is properly mentioned in db")
        logger.info("Expected--->" + expectedUserRole)
        logger.info("Actual  --->" + actualUserRoleDB)


    else:
        logger.error("user role is not properly mentioned db")
        logger.info("Expected--->" + expectedUserRole)
        logger.info("Actual  --->" + actualUserRoleDB)

    if actualUserRoleUI == actualUserRoleDB:
        logger.info("user role is same in the db and ui")
        logger.info("actualUserRoleUI--->" + actualUserRoleUI)
        logger.info("actualUserRoleDB  --->" + actualUserRoleDB)

    else:
        logger.error("user role is not same in the db and ui")
        logger.error("actualUserRoleUI--->" + actualUserRoleUI)
        logger.error("actualUserRoleDB  --->" + actualUserRoleDB)

    actualActionTypeUI = driver.find_element(By.XPATH, "//tbody[@role='presentation']/tr[2]/td[7]").text

    if actualActionTypeUI == expectedActionType:
        logger.info("action type is properly mentioned in UI")
        logger.info("Expected--->" + expectedActionType)
        logger.info("Actual  --->" + actualActionTypeUI)

    else:
        logger.error("action type is not properly mentioned in UI")
        logger.info("Expected--->" + expectedActionType)
        logger.info("Actual  --->" + actualActionTypeUI)

    actionTypeQuery = "select sactiontype from auditaction where nauditcode=(select COUNT(*) from auditaction )"

    actualActionTypeDB = JDBC.retunOneValue(actionTypeQuery)

    if actualActionTypeDB == expectedActionType:
        logger.info("action type is properly mentioned in db")
        logger.info("Expected--->" + expectedActionType)
        logger.info("Actual  --->" + actualActionTypeDB)

    else:
        logger.error("action type is not properly mentioned db")
        logger.error("Expected--->" + expectedActionType)
        logger.error("Actual  --->" + actualActionTypeDB)

    if actualActionTypeDB == actualActionTypeUI:
        logger.info("action type is same in the db and ui")
        logger.info("actualActionTypeDB--->" + actualActionTypeDB)
        logger.info("actualActionTypeUI  --->" + actualActionTypeUI)
    else:
        logger.error("action type is not same in the db and ui")
        logger.error("actualActionTypeDB--->" + actualActionTypeDB)
        logger.error("actualActionTypeUI  --->" + actualActionTypeUI)

    actualModuleNameUI = driver.find_element(By.XPATH, "//tbody[@role='presentation']/tr[2]/td[8]").text

    if actualModuleNameUI == expectedModuleName:
        logger.info("Expected--->" + expectedModuleName)
        logger.info("Actual  --->" + actualModuleNameUI)
        logger.info("Module name is properly mentioned in UI")

    else:
        logger.error("Module name  is not properly mentioned in UI")
        logger.error("Expected--->" + expectedModuleName)
        logger.error("Actual  --->" + actualModuleNameUI)

    moduleNameQuery = "select smodulename from qualismodule where nmodulecode=(select nmodulecode from auditaction where nauditcode=(select COUNT(*) from auditaction ))"

    actualModuleNameDB = JDBC.retunOneValue(moduleNameQuery)

    if actualModuleNameDB == expectedModuleName:

        logger.info("module is properly mentioned in db")
        logger.info("Expected--->" + expectedActionType)
        logger.info("Actual  --->" + actualModuleNameDB)
    else:
        logger.error("module is not properly mentioned db")
        logger.error("Expected--->" + expectedActionType)
        logger.error("Actual  --->" + actualModuleNameDB)

    if actualModuleNameDB == actualModuleNameUI:
        logger.info("module is same in the db and ui")
        logger.info("actualModuleNameDB--->" + actualModuleNameDB)
        logger.info("actualModuleNameUI  --->" + actualModuleNameUI)
    else:
        logger.error("module is not same in the db and ui")
        logger.error("actualModuleNameDB--->" + actualModuleNameDB)
        logger.error("actualModuleNameUI  --->" + actualModuleNameUI)

    actualFormNameUI = driver.find_element(By.XPATH, "//tbody[@role='presentation']/tr[2]/td[9]").text

    if actualFormNameUI == expectedFormName:
        logger.info("form name is properly mentioned in UI")
        logger.info("Expected--->" + expectedModuleName)
        logger.info("Actual  --->" + actualFormNameUI)

    else:
        logger.error("form name  is not properly mentioned in UI")
        logger.error("Expected--->" + expectedModuleName)
        logger.error("Actual  --->" + actualFormNameUI)

    formNameQuery = "select sformname from qualisforms where nformcode=(select nformcode from auditaction where nauditcode=(select COUNT(*) from auditaction )) and nformcode<>-2"
    actualFormNameDB = JDBC.retunOneValue(formNameQuery)

    if actualFormNameDB == expectedFormName:
        logger.info("form is properly mentioned in db")

        logger.info("Expected--->" + expectedFormName)
        logger.info("Actual  --->" + actualFormNameDB)

    else:
        logger.error("form is not properly mentioned db")

        logger.error("Expected--->" + expectedFormName)
        logger.error("Actual  --->" + actualFormNameDB)

    if actualFormNameUI == actualFormNameDB:
        logger.info("form is same in the db and ui")
        logger.info("actualFormNameUI--->" + actualFormNameUI)
        logger.info("actualFormNameDB  --->" + actualFormNameDB)
    else:
        logger.error("form is not same in the db and ui")
        logger.error("actualFormNameUI--->" + actualFormNameUI)
        logger.error("actualFormNameDB  --->" + actualFormNameDB)

    actualEsignCommentsUI = driver.find_element(By.XPATH, "//tbody[@role='presentation']/tr[2]/td[10]").text

    if actualEsignCommentsUI == expectedEsignComments:
        logger.info("Esign comment name is properly mentioned in UI")
        logger.info("Expected--->" + expectedEsignComments)
        logger.info("Actual  --->" + actualEsignCommentsUI)

    else:
        logger.error("Esign comment name  is not properly mentioned in UI")
        logger.error("Expected--->" + expectedEsignComments)
        logger.error("Actual  --->" + actualEsignCommentsUI)

    esignCommentQuery = "select sreason from auditaction where nauditcode=(select COUNT(*) from auditaction ) order by 1 desc"

    actualEsignCommentsDB = JDBC.retunOneValue(esignCommentQuery)

    if actualEsignCommentsDB == expectedEsignComments:
        logger.info("Esign comment is properly mentioned in db")
        logger.info("Expected--->" + expectedEsignComments)
        logger.info("Actual  --->" + actualEsignCommentsDB)
    else:
        logger.error("Esign comment is not properly mentioned db")
        logger.info("Expected--->" + expectedEsignComments)
        logger.info("Actual  --->" + actualEsignCommentsDB)

    if actualEsignCommentsDB == actualEsignCommentsUI:
        logger.info("Esign comment is same in the db and ui")
        logger.info("actualEsignCommentsDB--->" + actualEsignCommentsDB)
        logger.info("actualEsignCommentsUI  --->" + actualEsignCommentsUI)

    else:
        logger.error("Esign comment is not same in the db and ui")
        logger.error("actualEsignCommentsDB--->" + actualEsignCommentsDB)
        logger.error("actualEsignCommentsUI  --->" + actualEsignCommentsUI)



