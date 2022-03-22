from configparser import ConfigParser

from selenium.webdriver.common.by import By

from Utility import ScreenNavigate, BrowserOperation, BasicOperation

auditTrail=ConfigParser()
auditTrail.read(BasicOperation.projectDirectory()+"\\ObjectRepository\\ElementUserManagement.ini")




def auditTrailRecordCount(driver):

    ScreenNavigate.auditTrailPreCondition(driver)

    countText= driver.find_element(By.XPATH,"(//*[@class='k-pager-info k-label'])[2]").text

    print(countText)

    individualText=countText.split(' ')

    count=individualText[4]

    count=int(count)

    ScreenNavigate.auditTrailPostCondition(driver)

    return count






