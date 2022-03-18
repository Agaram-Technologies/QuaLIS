from Utility import BasicOperation
from Utility.BrowserOperation import configDriver


def unitAdd():
    pass


def unitEdit(driver):
    BasicOperation.clickXpath(driver, configDriver.get("UnitOfMeasurement", "masterIcon"))

    BasicOperation.clickXpath(driver, configDriver.get("UnitOfMeasurement", "baseMasterIcon"))

    BasicOperation.clickXpath(driver, configDriver.get("UnitOfMeasurement", "unitOfMeasurementIcon"))

