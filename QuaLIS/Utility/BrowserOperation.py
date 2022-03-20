import os
import time
from configparser import ConfigParser

from selenium import webdriver
from selenium.webdriver.common.by import By

from Utility import BasicOperation, LogOperation

projectDirectory=BasicOperation.projectDirectory()


configDriver=ConfigParser()
configDriver.read("..\config.ini")

objectRepository=ConfigParser()
objectRepository.read(projectDirectory+"\\ObjectRepository\\ElementLogin.ini")



def launchLIMS():

    try:
        driver = webdriver.Chrome(executable_path="..\chromedriver.exe")
        LogOperation.logInfo("Browser Launched")
        print("Browser Launched")
        driver.maximize_window()
        driver.implicitly_wait(20)

        try:
            driver.get(configDriver.get("Credential", "link"))
            LogOperation.logInfo("Link was hit")
            print("Link was hit")

            try:
                BasicOperation.sendKeysXpath(driver, objectRepository.get("login", "loginid"),
                                             configDriver.get("Credential", "loginid"))
                LogOperation.logInfo("Entered Login id")
                print("Entered Login id")

                try:

                    time.sleep(4)
                    BasicOperation.clickXpath(driver, objectRepository.get("login", "password"))

                    BasicOperation.sendKeysXpath(driver, objectRepository.get("login", "password"),
                                                 configDriver.get("Credential", "password"))
                    LogOperation.logInfo("Entered password id")

                    print("Entered password id")

                    try:
                        time.sleep(3)
                        BasicOperation.clickXpath(driver, objectRepository.get("login", "login"))
                        LogOperation.logInfo("Clicked the login button")

                        print("Clicked the login button")


                        i=0
                        while i<1:
                            title = driver.current_url
                            print(title)
                            if title=="http://192.168.0.199:9091/QuaLISWeb/#/home":
                                print("satisified")
                                break
                            else:
                                BasicOperation.clear(driver, objectRepository.get("login", "loginid"),
                                                             )
                                BasicOperation.sendKeysXpath(driver, objectRepository.get("login", "loginid"),
                                                             configDriver.get("Credential", "loginid"))

                                BasicOperation.sendKeysXpath(driver, objectRepository.get("login", "password"),
                                                             configDriver.get("Credential", "password"))

                                BasicOperation.clickXpath(driver, objectRepository.get("login", "login"))

                                print("not satisfied")


                            time.sleep(1)
                            i=i+1




                    except Exception as e:
                        LogOperation.logError("Tried to click the login button, It causes exception" + str(e))

                except Exception as e:
                    LogOperation.logError("Tried to enter the login id, It causes exception" + str(e))

            except Exception as e:
                LogOperation.logError("Tried to enter the login id, It causes exception" + str(e))

        except Exception as e:
            LogOperation.logError("Unable to hit the application, It causes exception" + str(e))



    except Exception as e:
        LogOperation.logError("Browser is not Launched, It caused exception " + str(e))

    return driver


launchLIMS()