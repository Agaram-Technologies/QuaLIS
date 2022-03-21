from configparser import ConfigParser

from Utility import BasicOperation

baseMaster=ConfigParser()
baseMaster.read(BasicOperation.projectDirectory()+"\\ObjectRepository\\ElementBaseMaster.ini")


def unit(driver):
    BasicOperation.clickXpath(driver,baseMaster.get("UnitOfMeasurement","masterIcon"))

    BasicOperation.clickXpath(driver, baseMaster.get("UnitOfMeasurement", "baseMasterIcon"))

    BasicOperation.clickXpath(driver, baseMaster.get("UnitOfMeasurement", "unitOfMeasurementIcon"))


