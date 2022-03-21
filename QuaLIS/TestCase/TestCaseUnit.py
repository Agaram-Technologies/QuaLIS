import os
import time

from TestCoverage import TestCoverageUnit
from Utility import BrowserOperation

driver=BrowserOperation.launchLIMS()

TestCoverageUnit.unitAdd(driver,"d","dd")

#TestCoverageUnit.unitDelete(driver,"d")



