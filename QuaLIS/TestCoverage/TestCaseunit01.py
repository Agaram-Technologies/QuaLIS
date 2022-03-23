from TestCoverage import TestCoverageUnit
from Utility import BrowserOperation

driver=BrowserOperation.launchLIMS()

oldName="100"

oldDescription="100des"

newName="200"

newDescription="200ds"

TestCoverageUnit.unitAdd(driver,oldName,oldDescription,"No")

BrowserOperation.refreshLogin(driver)

TestCoverageUnit.unitEdit(driver,oldName,oldDescription,"No",newName,newDescription)

BrowserOperation.refreshLogin(driver)

TestCoverageUnit.unitDelete(driver,newName,newDescription,"No")

BrowserOperation.refreshLogin(driver)

