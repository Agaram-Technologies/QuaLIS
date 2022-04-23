from TestCoverage import TestCoverageUnit
from Utility import BrowserOperation, BasicOperation


driver=BrowserOperation.launchLIMS()

TestCoverageUnit.unitDuplicate(driver)

