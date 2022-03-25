import pytest

import allure

from TestCoverage import TestCoverageUnit
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
    TestCoverageUnit.unitAdd(driver, oldName, oldDescription, "Yes")
    BrowserOperation.refreshLogin(driver)


def test_unitEdit():
    TestCoverageUnit.unitEdit(driver, oldName, oldDescription, "No", newName, newDescription)
    BrowserOperation.refreshLogin(driver)


def test_unitDelete():
    TestCoverageUnit.unitDelete(driver, newName, newDescription, "Yes")
    BrowserOperation.refreshLogin(driver)

def test_exportPDF():
    TestCoverageUnit.downloadExcel(driver)
    BrowserOperation.refreshLogin(driver)

def test_exportEXCEL():
    TestCoverageUnit.downloadPDF(driver)
    BrowserOperation.refreshLogin(driver)


def test_auditTrailUnitAdd():
    TestCoverageUnit.auditTrailUnitAdd(driver,oldName,oldDescription,"No")


def test_auditTrailUnitEdit():
    TestCoverageUnit.auditTrailUnitEdit(driver, oldName, oldDescription, newName, newDescription, "oldDefaultStatus")

def test_auditTrailUnitDelete():
    TestCoverageUnit.auditTrailUnitDelete(driver, oldName, oldDescription, "No")

def test_filter():
    TestCoverageUnit.unitFilter(driver)





