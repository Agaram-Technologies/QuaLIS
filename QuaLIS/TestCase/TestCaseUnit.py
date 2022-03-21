import os
import time
from configparser import ConfigParser

from TestCoverage import TestCoverageUnit
from Utility import BrowserOperation, BasicOperation



driver=BrowserOperation.launchLIMS()

TestCoverageUnit.unitAdd(driver,"d","dd")

#TestCoverageUnit.unitDelete(driver,"d")



