from configparser import ConfigParser

from TestCoverage import TestCoverageUnit, TestCoverageAudittrail
from Utility import BrowserOperation, BasicOperation

name=BasicOperation.timet()[11:]

description="cm1"

unit=ConfigParser()
unit.read(BasicOperation.projectDirectory()+"\\TestData\\TestDataUnit.ini")

driver=BrowserOperation.launchLIMS()

TestCoverageUnit.downloadExcel(driver)

TestCoverageUnit.downloadPDF(driver)



#TestCoverageUnit.unitAdd(driver,unit.get("Add","name"),unit.get("Add","description"),"No")

#TestCoverageUnit.auditTrailUnitAdd(driver,name,description,"No")

#TestCoverageUnit.unitDelete(driver,name)



