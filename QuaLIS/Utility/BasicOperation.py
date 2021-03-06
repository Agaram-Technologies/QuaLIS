import os
from datetime import datetime

import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def timet():
    currentsysdatetime = datetime.today()
    usrsysdatetime = currentsysdatetime.strftime("%d/%m/%Y %H:%M:%S")
    print(usrsysdatetime+"")
    return usrsysdatetime

def clickXpath(driver,xpath):

    element=driver.find_element(By.XPATH,xpath)

    try:
        element.click()

    except:
        time.sleep(5)
        element.click()

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



def scrollToElement(driver,xpath):
   element=driver.find_element(By.XPATH,xpath)

   driver.execute_script("arguments[0].scrollIntoView();", element)



def screenshot(driver,location):
    driver.save_screenshot(location)


def exceptionClick(driver,xpath):

    element=driver.find_element(By.XPATH,xpath)
    exception=True

    x=1000

    for i in range(0,x):
        print(i)
        if exception==False:
            break

        try:
            element.click()

            exception=False

            if exception==False:
                break

        except:
            time.sleep(1)

            print("exception occured ")

            try:
                element.click()

                exception = False

                if(exception==False):
                    break

            except:
                print("exception occured ")





def selectByVisibleText(driver,element,option):

    driver.find_element(By.XPATH,element).click()

    time.sleep(2)

    optionXpath="//*[text()='{}']".format(option)

    print(optionXpath)

    driver.find_element(By.XPATH,optionXpath).click()



def wait(driver,element,time):

    wait = WebDriverWait(driver, time)

    result = wait.until(expected_conditions.element_to_be_clickable(element))

    print(result)

def totalCount(driver,xpath):

    text=driver.find_element(By.XPATH,xpath).text

    textList=text.split(' ')

    count=textList[len(textList)-1]

    return count


