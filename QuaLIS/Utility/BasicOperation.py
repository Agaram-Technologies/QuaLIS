import os
from datetime import datetime

import time

from selenium.webdriver.common.by import By


def timet():
    currentsysdatetime = datetime.today()
    usrsysdatetime = currentsysdatetime.strftime("%d/%m/%Y %H:%M:%S")
    print(usrsysdatetime+"")
    return usrsysdatetime

def clickXpath(driver,xpath):
   driver.find_element(By.XPATH,xpath).click()

def sendKeysXpath(driver,xpath,value):
    driver.find_element(By.XPATH,xpath).send_keys(value)

def listOfElements(driver,xpath):
   listOfElements= driver.find_elements(By.XPATH,xpath)
   return listOfElements

def clear(driver,xpath):
    driver.find_element(By.XPATH,xpath).clear()

def screenshot(driver,location):
    driver.save_screenshot(location)


def projectDirectory():

    projectDirectory=""

    fileDirectory=os.path.abspath(__file__)

    fileDirectoryArray=fileDirectory.split("\\")

    for i in fileDirectoryArray:

        projectDirectory=projectDirectory+"\\"+i
        if i=="QuaLIS":
             break

    projectDirectory=projectDirectory[1:]

    print(projectDirectory)

    return projectDirectory

projectDirectory()




def elementByText(driver,text):
    driver.find_element(By.XPATH,"//*[text()='{}']".format(text)).click()




def getText(driver,xpath):
   text= driver.find_element(By.XPATH,xpath).text
   return text



def auditTrailCount(text):



    textList=text.split(' ')

    count=len(textList)-1

    return int(count)



def scrollClickXpath(driver,xpath):
   element=driver.find_element(By.XPATH,xpath).click()

   driver.execute_script("arguments[0].scrollIntoView();", element)

   time.sleep(2)

   element.click()




