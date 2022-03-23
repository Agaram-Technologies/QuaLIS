from Utility import BasicOperation, LogOperation


def exceptionClick(driver,xpath,info,error):
    try:
        BasicOperation.clickXpath(driver,xpath)
        LogOperation.logInfo(info)
    except Exception as e:
        LogOperation.logError(error+str(e))


