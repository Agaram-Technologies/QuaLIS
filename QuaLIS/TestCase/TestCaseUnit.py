import pytest

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

@pytest.mark.skip(reason="no way of currently testing this")
def test_unitAdd(preCondition):
    TestCoverageUnit.unitAdd(driver, oldName, oldDescription, "No")
    BrowserOperation.refreshLogin(driver)

@pytest.mark.skip(reason="no way of currently testing this")
def test_unitEdit():
    TestCoverageUnit.unitEdit(driver, oldName, oldDescription, "No", newName, newDescription)
    BrowserOperation.refreshLogin(driver)

@pytest.mark.skip(reason="no way of currently testing this")
def test_unitDelete():
    TestCoverageUnit.unitDelete(driver, newName, newDescription, "No")
    BrowserOperation.refreshLogin(driver)

@pytest.mark.skip(reason="no way of currently testing this")
def test_exportPDF():
    TestCoverageUnit.downloadExcel(driver)
    BrowserOperation.refreshLogin(driver)

@pytest.mark.skip(reason="no way of currently testing this")
def test_exportEXCEL():
    TestCoverageUnit.downloadPDF(driver)
    BrowserOperation.refreshLogin(driver)

@pytest.mark.skip(reason="no way of currently testing this")
def test_auditTrailUnitAdd(preCondition):
    TestCoverageUnit.auditTrailUnitAdd(driver,oldName,oldDescription,"No")

oldName="200"
oldDescription="dd"
@pytest.mark.skip(reason="no way of currently testing this")
def test_auditTrailUnitEdit(preCondition):
    TestCoverageUnit.auditTrailUnitEdit(driver, oldName, oldDescription, newName, newDescription, "oldDefaultStatus")

def test_auditTrailUnitDelete(preCondition):
    TestCoverageUnit.auditTrailUnitDelete(driver, oldName, oldDescription, "No")





