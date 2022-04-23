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



@pytest.fixture(scope="function")
def preCondition():
    global driver
    driver = BrowserOperation.launchLIMS()


def test_Add(preCondition):

    TestCoverageStorageCondition.storageConditionAdd(driver, oldName, oldDescription, "yes")
    BrowserOperation.refreshLogin(driver)




def test_Edit():
    TestCoverageStorageCondition.storageConditionEdit(driver, oldName, oldDescription, "No", newName, newDescription)
    BrowserOperation.refreshLogin(driver)



def test_Delete():
    TestCoverageStorageCondition.storageConditionDelete(driver, newName, newDescription, "Yes")
    BrowserOperation.refreshLogin(driver)

    time.sleep(2)

def test_exportEXCEL():

    TestCoverageStorageCondition.downloadExcel(driver)
    BrowserOperation.refreshLogin(driver)
    time.sleep(2)

def test_exportPDF():
    TestCoverageStorageCondition.downloadPDF(driver)

    BrowserOperation.refreshLogin(driver)
    time.sleep(2)


