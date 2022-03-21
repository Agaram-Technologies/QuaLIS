from configparser import ConfigParser

from Utility import BasicOperation

baseMaster=ConfigParser()
baseMaster.read(BasicOperation.projectDirectory()+"\\ObjectRepository\\ElementBaseMaster.ini")

auditTrail=ConfigParser()
auditTrail.read(BasicOperation.projectDirectory()+"\\ObjectRepository\\ElementUserManagement.ini")

def unit(driver):
    BasicOperation.clickXpath(driver,baseMaster.get("UnitOfMeasurement","masterIcon"))

    BasicOperation.clickXpath(driver, baseMaster.get("UnitOfMeasurement", "baseMasterIcon"))

    BasicOperation.clickXpath(driver, baseMaster.get("UnitOfMeasurement", "unitOfMeasurementIcon"))


def auditTrail(driver):
    BasicOperation.clickXpath(driver,auditTrail.get("AuditTrail","masterIcon"))

    BasicOperation.clickXpath(driver, auditTrail.get("AuditTrail", "userManagementIcon"))

    BasicOperation.clickXpath(driver, auditTrail.get("AuditTrail", "auditTrailIcon"))