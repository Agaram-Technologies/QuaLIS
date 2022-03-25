import pytest

import allure

from TestCoverage import TestCoverageUnit
from Utility import BrowserOperation

oldName="100"

oldDescription="100des"

newName="200"

newDescription="200ds"


driver = BrowserOperation.launchLIMS()

TestCoverageUnit.unitEdit(driver, oldName, oldDescription, "No", newName, newDescription)

TestCoverageUnit.unitAdd(driver, oldName, oldDescription, "Yes")


