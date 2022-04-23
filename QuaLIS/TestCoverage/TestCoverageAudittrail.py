import time
from configparser import ConfigParser

from loguru import logger
from selenium.webdriver.common.by import By

from Utility import ScreenNavigate, BrowserOperation, BasicOperation

auditTrail=ConfigParser()
auditTrail.read(BasicOperation.projectDirectory()+"\\ObjectRepository\\ElementUserManagement.ini")




def auditTrailRecordCount(driver):

    ScreenNavigate.auditTrailPreCondition(driver)

    try:
        countText= driver.find_element(By.XPATH,"(//*[@class='k-pager-info k-label'])[2]").text

        individualText = countText.split(' ')

        count = individualText[4]

        logger.info("The count is fetched, it shows {} record in the grid".format(count))

        count = int(count)

    except:

        try:
            time.sleep(3)

            countText = driver.find_element(By.XPATH, "(//*[@class='k-pager-info k-label'])[2]").text

            individualText = countText.split(' ')

            count = individualText[4]

            logger.info("The count is fetched, it shows {} record in the grid".format(count))

            count = int(count)

        except:

            logger.error("Unable to get the count in the Audit trail screen")


    ScreenNavigate.auditTrailPostCondition(driver)

    return count






