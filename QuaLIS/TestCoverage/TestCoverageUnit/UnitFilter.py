from Utility import BrowserOperation

BrowserOperation.launchLIMS()


from configparser import ConfigParser


from Utility import BasicOperation, ScreenNavigate, BrowserOperation

driver=BrowserOperation.launchLIMS()

baseMaster=ConfigParser()
baseMaster.read(BasicOperation.projectDirectory()+"\\ObjectRepository\\ElementBaseMaster.ini")

def unitSearch(driver):
    ScreenNavigate.unit(driver)

    BasicOperation.clickXpath(driver,baseMaster.get("UnitOfMeasurement","unitNameFilter"))





unitSearch(driver)
