from configparser import ConfigParser

from Utility import ScreenNavigate, BrowserOperation, BasicOperation

auditTrail=ConfigParser()
auditTrail.read(BasicOperation.projectDirectory()+"\\ObjectRepository\\ElementUserManagement.ini")




def auditTrailRecordCount(driver):

    ScreenNavigate.auditTrail(driver)

    countText= BasicOperation.getText( auditTrail.get("AuditTrail", "countText"))

    count=BasicOperation.auditTrailCount(countText)

    return count




driver=BrowserOperation.launchLIMS()

