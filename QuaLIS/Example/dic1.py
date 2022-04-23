import time
from configparser import ConfigParser

from loguru import logger
from selenium.webdriver.common.by import By

from Utility import BasicOperation, BrowserOperation, ScreenNavigate

objectRepository=ConfigParser()
objectRepository.read("D:\\Agaram Technologies\\Github\\QuaLIS\\ObjectRepository\\filter.ini")




def containerType_search(driver, loc_key, filterdata):
    containerType_filtericon = objectRepository.get(loc_key, "containertypefiltericon_filterbutton")
    containerType_filtericon_contains = objectRepository.get(loc_key, "containertypefiltericon_contains")
    containerType_filtericon_containstextfield = objectRepository.get(loc_key, "containertypefiltericon_contains_textfield")
    containerType_filtericon_and = objectRepository.get(loc_key, "containertypefiltericon_And")
    containerType_filtericon_and_contains = objectRepository.get(loc_key, "containertypefiltericon_Andcontains")
    containerType_filtericon_and_contains_textfield = objectRepository.get(loc_key, "containertypefiltericon_Andcontains_textfield")
    containerType_filtericon_filterbutton = objectRepository.get(loc_key, "containertypefiltericon_filterbutton")
    containerType_filtericon_clearbutton = objectRepository.get(loc_key, "containertypefiltericon_clearbutton")

    time.sleep(7)

    try:
        BasicOperation.clickXpath(driver, "//*[@id='content']/div[2]/div/div/div/div[2]/div/div[2]/div/table/thead/tr/th[1]/div/div/span")

        BasicOperation.clickXpath(driver, containerType_filtericon_contains)
        time.sleep(2)

        element = driver.find_element(By.XPATH, "//*[text()='Is equal to']")
        driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(2)
        element.click()

        time.sleep(2)

        BasicOperation.clickXpath(driver, containerType_filtericon_and)
        time.sleep(2)

        element = driver.find_element(By.XPATH, "//*[text()='Or']")
        driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(2)
        element.click()

        time.sleep(2)
        BasicOperation.clickXpath(driver, containerType_filtericon_and_contains)
        time.sleep(2)

        element = driver.find_element(By.XPATH, "//*[text()='Starts with']")
        driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(2)
        element.click()

        time.sleep(2)

        time.sleep(2)
        BasicOperation.clickXpath(driver, containerType_filtericon_filterbutton)

        logger.info("ContainerType data filtered")

        BasicOperation.sendKeysXpath(driver, containerType_filtericon_and_contains_textfield,
                                     containerType_filtericon_and_contains_textfieldvalue)

    except Exception as e :
        logger.error("ContainerType data not filtered" +str(e))


    time.sleep(2)

    try:
        BasicOperation.clickXpath(driver, containerType_refreshbutton)
        logger.info("ContainerType Screen refreshed")

    except Exception as e:
        logger.error("ContainerType Screen has not refreshed")









driver=BrowserOperation.launchLIMS()

ScreenNavigate.unit(driver)

containerType_search(driver,"containertype","d")