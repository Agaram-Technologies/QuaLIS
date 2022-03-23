from Utility import BasicOperation, LogOperation


def exceptionClick(driver,xpath,info,error):
    try:
        BasicOperation.clickXpath(driver,xpath)
        LogOperation.logInfo(info)
    except Exception as e:
        LogOperation.logError(error+str(e))


def exceptionSendKeys(driver,xpath,value,info,error):
    try:
        BasicOperation.sendKeysXpath(driver,xpath,value)
        LogOperation.logInfo(info)
    except Exception as e:
        LogOperation.logError(error+str(e))


