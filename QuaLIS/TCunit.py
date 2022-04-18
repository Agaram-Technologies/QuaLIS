import time

from CommonMethodNameDescriptionDefaultStatus import AddAllFieldDefaultYes
from Config.ScreenshotPath import ScreenshotUnit
from ObjectRepository.BaseMaster import ElementUnit
from TestCoverage import TestCoverageUnit
from TestData import TestDataUnit
from Utility import BrowserOperation

oldName="100"

oldDescription="100des"

newName="200"

newDescription="200ds"

driver=BrowserOperation.launchLIMS()

'''
AddAllFieldDefaultYes.addFieldValueDefaultYes(driver, ElementUnit.elementUnit(),ScreenshotUnit.screenshotUnitAddAllFieldDefaultYes(), TestDataUnit.unit())

BrowserOperation.refreshLogin(driver)

TestCoverageUnit.unitEdit(driver, oldName, oldDescription, "Yes", newName, newDescription)

BrowserOperation.refreshLogin(driver)

TestCoverageUnit.unitDelete(driver, newName, newDescription, "Yes")


BrowserOperation.refreshLogin(driver)

'''

TestCoverageUnit.downloadExcel(driver)

BrowserOperation.refreshLogin(driver)

TestCoverageUnit.downloadPDF(driver)

BrowserOperation.refreshLogin(driver)



'''



#TestCoverageUnit.auditTrailUnitAdd(driver,oldName,oldDescription,"No")


def test_auditTrailUnitEdit():
    TestCoverageUnit.auditTrailUnitEdit(driver, oldName, oldDescription, newName, newDescription, "oldDefaultStatus")

def test_auditTrailUnitDelete():
    TestCoverageUnit.auditTrailUnitDelete(driver, oldName, oldDescription, "No")

def test_filter():
    TestCoverageUnit.unitFilter(driver)
'''