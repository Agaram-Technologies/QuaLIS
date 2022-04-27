from datetime import datetime

from loguru import logger

from ObjectRepository import ElementAuditTrail
from TestCoverage import TestCoverageUnit, TestCoverageAudittrail
from Utility import BrowserOperation, JDBC

time=datetime.now()


oldName= str(time)

oldDescription="centimeter"

newName=oldName+"d"


newDescription="Milli meter"

driver=BrowserOperation.launchLIMS()

TestCoverageUnit.auditTrailUnitAdd(driver, "temperature", oldDescription, "No")



'''

def auditTrailUnitAdd(driver,name,description,defaultStatus):

    esign=""

    beforeCount=TestCoverageAudittrail.auditTrailRecordCount(driver)
    
    esign=""

    query = "select sfirstname from users where sloginid='{}'".format(id)

    query2 = "select sfirstname from users where sloginid='{}'".format(id)

    userName=JDBC.retunOneValue(query)+" "+JDBC.retunOneValue(query2)


    output = unitAdd(driver, name, description, "No")

    configDriver = ConfigParser()

    configDriver.read(BasicOperation.projectDirectory() + "\\config.ini")

    userRole=configDriver.get("Credential","userRole")

    auditTrailRecord={"AuditDateAndTime":output.get("addtime"),"AuditAction":"ADD UNIT","comments":"Unit Name: {};Description: {};Default Status: No;".format(name,description),"userName":"{}".format(userName),"userRole":"{}".format(userRole),"ActionType":"SYSTEM","ModuleName":"Base Master","FormName":"Unit of Measurement","esignComments":"{}".format(esign)}

    expectedAuditAction= auditTrailRecord.get("AuditAction")

    expectedComments=auditTrailRecord.get("comments")

    expectedUserName=auditTrailRecord.get("userName")

    expectedUserRole=auditTrailRecord.get("userRole")

    expectedActionType = auditTrailRecord.get("ActionType")

    expectedModuleName  = auditTrailRecord.get("ModuleName")

    expectedFormName = auditTrailRecord.get("FormName")

    expectedEsignComments = auditTrailRecord.get("esignComments")

    #expectedTime=auditTrailRecord.get("addtime")[0:15]

    time.sleep(3)

    afterCount=TestCoverageAudittrail.auditTrailRecordCount(driver)

    logger.info("After count is "+str(afterCount))

    auditActionList=driver.find_elements(By.XPATH, "//tbody[@role='presentation']/tr[2]/td[2]")

    if afterCount==beforeCount:
        ResultCase1="FAIL"
        result="Audit trail is not captured"
        logger.error(result)

    elif afterCount==beforeCount+1:

        i=2

        ResultCase1 = "PASS"

        result="Audit trail is captured"

        logger.info(result)

        # actualAuditDateAndTime=driver.find_element(By.XPATH,"//tbody[@role='presentation']/tr[2]/td[2]").text
        #
        # auditTime=actualAuditDateAndTime[0:15]
        #
        # if expectedTime.__contains__(auditTime):
        #     logger.info("Login time shows correctly")
        # else:
        #     logger.error("Time detail is not  shown correctly")


        actualAuditActionUI=driver.find_element(By.XPATH,"//tbody[@role='presentation']/tr[2]/td[3]").text

        if actualAuditActionUI==expectedAuditAction:

            logger.info("Audit action is properly mentioned in UI")

        else:
            logger.error("Audit action is not properly mentioned in UI")

        actualAuditActionDB=JDBC.retunOneValue("select sauditaction from auditaction where nauditcode=(select COUNT(*) from auditaction )")


        if actualAuditActionDB==expectedAuditAction:

            logger.info("Audit action is properly mentioned in db")

        else:
            logger.error("Audit action is not properly mentioned db")

        if actualAuditActionUI==actualAuditActionDB:
            logger.info("Audit action is same in the db and ui")

        else:
            logger.error("Audit action is not same in the db and ui")

        actualCommentsUI = driver.find_element(By.XPATH,"//tbody[@role='presentation']/tr[2]/td[4]").text

        if actualCommentsUI==expectedComments:

            logger.info("Audit comment is properly mentioned in UI")

        else:
            logger.error("Audit comment is not properly mentioned in UI")



        actualUserNameUI = driver.find_element(By.XPATH,"//tbody[@role='presentation']/tr[2]/td[5]").text


        if actualUserNameUI==expectedUserName:

            logger.info("user name is properly mentioned in UI")

        else:
            logger.error("user name is not properly mentioned in UI")



        actualUserRoleUI = driver.find_element(By.XPATH,"//tbody[@role='presentation']/tr[2]/td[6]").text



        if actualUserRoleUI==expectedUserRole:

            logger.info("user role is properly mentioned in UI")

        else:
            logger.error("Audit action is not properly mentioned in UI")

        queryr="select suserrolename from userrole where nuserrolecode=(select nuserrole from auditaction where nauditcode=(select COUNT(*) from auditaction ))"

        actualUserRoleDB=JDBC.retunOneValue(queryr)


        if actualUserRoleDB==expectedUserRole:

            logger.info("user role is properly mentioned in db")

        else:
            logger.error("user role is not properly mentioned db")

        if actualUserRoleUI==actualUserRoleDB:
            logger.info("user role is same in the db and ui")

        else:
            logger.error("user role is not same in the db and ui")


        actualActionTypeUI = driver.find_element(By.XPATH,"//tbody[@role='presentation']/tr[2]/td[7]").text

        if actualActionTypeUI == expectedActionType:

            logger.info("action type is properly mentioned in UI")

        else:
            logger.error("action type is not properly mentioned in UI")

        actionTypeQuery = "select sactiontype from auditaction where nauditcode=(select COUNT(*) from auditaction )"

        actualActionTypeDB = JDBC.retunOneValue(actionTypeQuery)

        if actualActionTypeDB == expectedActionType:

            logger.info("action type is properly mentioned in db")

        else:
            logger.error("action type is not properly mentioned db")

        if actualActionTypeDB == actualActionTypeUI:
            logger.info("action type is same in the db and ui")
        else:
            logger.error("action type is not same in the db and ui")

        actualModuleNameUI = driver.find_element(By.XPATH,"//tbody[@role='presentation']/tr[2]/td[8]").text

        if actualModuleNameUI == expectedModuleName:

            logger.info("Module name is properly mentioned in UI")

        else:
            logger.error("Module name  is not properly mentioned in UI")

        moduleNameQuery = "select smodulename from qualismodule where nmodulecode=(select nmodulecode from auditaction where nauditcode=(select COUNT(*) from auditaction ))"

        actualModuleNameDB = JDBC.retunOneValue(moduleNameQuery)

        if actualModuleNameDB == expectedActionType:

            logger.info("module is properly mentioned in db")

        else:
            logger.error("module is not properly mentioned db")

        if actualModuleNameDB == actualModuleNameUI:
            logger.info("module is same in the db and ui")
        else:
            logger.error("module is not same in the db and ui")


        actualFormNameUI = driver.find_element(By.XPATH,"//tbody[@role='presentation']/tr[2]/td[9]").text


        if actualFormNameUI == expectedModuleName:

            logger.info("form name is properly mentioned in UI")

        else:
            logger.error("form name  is not properly mentioned in UI")

        formNameQuery = "select sformname from qualisforms where nmodulecode=(select nmodulecode from auditaction where nauditcode=(select COUNT(*) from auditaction )) and nformcode<>-2"

        actualFormNameDB = JDBC.retunOneValue(formNameQuery)

        if  actualFormNameDB== expectedActionType:

            logger.info("form is properly mentioned in db")

        else:
            logger.error("form is not properly mentioned db")

        if actualFormNameUI == actualFormNameDB:
            logger.info("form is same in the db and ui")
        else:
            logger.error("form is not same in the db and ui")


        actualEsignCommentsUI = driver.find_element(By.XPATH,"//tbody[@role='presentation']/tr[2]/td[10]").text

        if actualEsignCommentsUI == expectedModuleName:

            logger.info("Esign comment name is properly mentioned in UI")

        else:
            logger.error("Esign comment name  is not properly mentioned in UI")

        esignCommentQuery = "select sreason from auditaction where nauditcode=(select COUNT(*) from auditaction ) order by 1 desc"

        actualEsignCommentsDB = JDBC.retunOneValue(esignCommentQuery)

        if actualEsignCommentsDB == expectedActionType:

            logger.info("Esign comment is properly mentioned in db")

        else:
            logger.error("Esign comment is not properly mentioned db")

        if actualEsignCommentsDB == actualEsignCommentsUI:
            logger.info("Esign comment is same in the db and ui")
        else:
            logger.error("Esign comment is not same in the db and ui")

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
                    '''


