from Utility import tc



from configparser import ConfigParser

from loguru import logger
from selenium.webdriver.common.by import By

from ObjectRepository import ElementAuditTrail
from TestCoverage import TestCoverageAudittrail, TestCoverageUnit
from Utility import JDBC, BasicOperation, BrowserOperation

configDriver=ConfigParser()
configDriver.read(BasicOperation.projectDirectory()+"\\config.ini")

id=configDriver.get("Credential", "loginid")
oldName="unique"

newName="unique1"

driver=BrowserOperation.launchLIMS()


tc.auditTrailUnitEdit(driver,oldName,oldName,newName,newName,"d")