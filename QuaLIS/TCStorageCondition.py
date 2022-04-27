import time

import pytest

import allure

from CommonMethodNameDescriptionDefaultStatus import AddAllFieldDefaultYes
from Config.ScreenshotPath import ScreenshotUnit
from ObjectRepository.BaseMaster import ElementUnit
from TestCoverage import TestCoverageUnit, TestCoverageContainerType, TestCoverageStorageCondition
from TestData import TestDataUnit
from Utility import BrowserOperation

oldName="100"

oldDescription="100des"

newName="200"

newDescription="200ds"



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


driver=BrowserOperation.launchLIMS()
#
# TestCoverageStorageCondition.storageConditionAdd(driver,oldName,oldDescription,"yes")
#
# TestCoverageStorageCondition.storageConditionEdit(driver,oldName,oldDescription,"yes",newName,newDescription)
#
# TestCoverageStorageCondition.storageConditionDelete(driver,newName,newDescription,"yes")

TestCoverageStorageCondition.auditTrailUnitAdd(driver,oldName,oldDescription,"yes")