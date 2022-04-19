import time

import pytest

import allure

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



@pytest.fixture(scope="function")
def preCondition():
    global driver
    driver = BrowserOperation.launchLIMS()


def test_unitAdd(preCondition):

    AddAllFieldDefaultYes.addFieldValueDefaultYes(driver, ElementUnit.elementUnit(),ScreenshotUnit.screenshotUnitAddAllFieldDefaultYes(), TestDataUnit.unit())
    BrowserOperation.refreshLogin(driver)
    time.sleep(2)

def test_unitEdit():
    TestCoverageUnit.unitEdit(driver, oldName, oldDescription, "No", newName, newDescription)
    BrowserOperation.refreshLogin(driver)
    time.sleep(2)


def test_unitDelete():
    TestCoverageUnit.unitDelete(driver, newName, newDescription, "Yes")
    BrowserOperation.refreshLogin(driver)
    time.sleep(2)

def test_exportEXCEL():
    TestCoverageUnit.downloadExcel(driver)
    BrowserOperation.refreshLogin(driver)
    time.sleep(2)

def test_exportPDF():
    TestCoverageUnit.downloadPDF(driver)
    BrowserOperation.refreshLogin(driver)
    time.sleep(2)
'''


def test_auditTrailUnitAdd():
    TestCoverageUnit.auditTrailUnitAdd(driver,oldName,oldDescription,"No")


def test_auditTrailUnitEdit():
    TestCoverageUnit.auditTrailUnitEdit(driver, oldName, oldDescription, newName, newDescription, "oldDefaultStatus")

def test_auditTrailUnitDelete():
    TestCoverageUnit.auditTrailUnitDelete(driver, oldName, oldDescription, "No")

def test_filter():
    TestCoverageUnit.unitFilter(driver)





'''