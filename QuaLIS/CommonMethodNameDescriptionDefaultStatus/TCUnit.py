from CommonMethodNameDescriptionDefaultStatus import AddAllFieldDefaultYes
from ObjectRepository.BaseMaster import ElementUnit, ElementStorageCondition
from TestData import TestDataUnit
from Utility import BrowserOperation



driver=BrowserOperation.launchLIMS()
#AddAllFieldDefaultYes.addFieldValueDefaultYes(driver,ElementStorageCondition.elementstorageCondition(),TestDataUnit.unit())

AddAllFieldDefaultYes.addFieldValueDefaultYes(driver,ElementUnit.elementUnit(),TestDataUnit.unit())



driver.close()