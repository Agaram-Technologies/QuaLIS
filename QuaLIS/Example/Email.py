from CommonMethodNameDescriptionDefaultStatus import AddAllFieldDefaultYes
from Config.ScreenshotPath import ScreenshotUnit
from ObjectRepository.BaseMaster import ElementUnit
from TestData import TestDataUnit
from Utility import BrowserOperation

driver=BrowserOperation.launchLIMS()

AddAllFieldDefaultYes.addFieldValueDefaultYes(driver, ElementUnit.elementUnit(),
                                              ScreenshotUnit.screenshotUnitAddAllFieldDefaultYes(), TestDataUnit.unit())
