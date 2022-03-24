from selenium.webdriver.common.by import By

from TestCoverage import TestCoverageUnit
from Utility import BrowserOperation

driver=BrowserOperation.launchLIMS()

TestCoverageUnit.unitAdd(driver, "oldName", "oldDescription", "No")


#TestCoverageUnit.unitFilter(driver)

