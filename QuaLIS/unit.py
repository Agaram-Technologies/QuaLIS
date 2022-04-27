import time
from configparser import ConfigParser
from datetime import datetime

from loguru import logger
from selenium.webdriver.common.by import By

from Example.s import configDriver
from TestCoverage import TestCoverageUnit, TestCoverageAudittrail
from Utility import BrowserOperation, BasicOperation, JDBC

time1=datetime.now()


oldName= "cm1"

oldDescription="centi meter"

newName="cm2"


newDescription="Milli meter"

driver=BrowserOperation.launchLIMS()

id="admin"

def auditTrailUnitDelete(driver,name,description,defaultStatus):

    esign=""

    query = "select sfirstname from users where sloginid='{}'".format(id)

    query2 = "select sfirstname from users where sloginid='{}'".format(id)

    userName=JDBC.retunOneValue(query)+" "+JDBC.retunOneValue(query2)


    beforeCount=TestCoverageAudittrail.auditTrailRecordCount(driver)

    TestCoverageUnit.unitDelete(driver, name, description, "No")

    logger.info("Got the count before delete it")

    userRole = configDriver.get("Credential", "userRole")

    auditTrailRecord={"AuditAction":"DELETE UNIT","comments":"Unit Name: {};Description: {};Default Status: No;	".format(name,description),"userName":"{}".format(userName),"userRole":"{}".format(userRole),"ActionType":"SYSTEM","ModuleName":"Base Master","FormName":"Unit of Measurement","esignComments":""}


    expectedAuditAction= auditTrailRecord.get("AuditAction")

    expectedComments=auditTrailRecord.get("comments")

    expectedUserName=auditTrailRecord.get("userName")

    expectedUserRole=auditTrailRecord.get("userRole")

    expectedActionType = auditTrailRecord.get("ActionType")

    expectedModuleName  = auditTrailRecord.get("ModuleName")

    expectedFormName = auditTrailRecord.get("FormName")

    expectedEsignComments = auditTrailRecord.get("esignComments")

    expectedAuditTrail={}

    expectedAuditTrail["expectedAuditAction"]=expectedAuditAction

    expectedAuditTrail["expectedEsignComments"]=expectedEsignComments

    expectedAuditTrail["expectedFormName"]=expectedFormName

    expectedAuditTrail["expectedModuleName"]=expectedModuleName

    expectedAuditTrail["expectedActionType"]=expectedActionType

    expectedAuditTrail["expectedUserRole"]=expectedUserRole

    expectedAuditTrail["expectedUserName"]=expectedUserName

    expectedAuditTrail["expectedComments"]=expectedComments

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


        TestCoverageUnit.auditTrail(driver,expectedAuditTrail)


auditTrailUnitDelete(driver, "cm2",newDescription, "yes")
