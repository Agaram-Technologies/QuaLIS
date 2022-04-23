import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Config import ObjectName
from Config.ScreenshotPath import ScreenshotUnit, ScreenshotName
from Utility import BasicOperation, LogOperation, BrowserOperation, JDBC


def addFieldValueDefaultYes(driver,element,screenshot,value):

     screenshot = dict(screenshot)

     value = dict(value)

     element = dict(element)

     module = element.get(ObjectName.module)

     subModule = element.get(ObjectName.subModule)

     screen = element.get(ObjectName.screen)

     navigatePermission="FAIL"

     try:

          BasicOperation.clickXpath(driver, element.get(ObjectName.moduleIcon))

          try:

               driver.save_screenshot(screenshot.get(ScreenshotName.moduleClick) + ".info.png")

               print("1. "+module+" click screenshot info is taken")

          except:
               print("1. "+module+" click screenshot info not taken")

          navigatePermission = "PASS"

          result = "Clicked the "+module+" Icon"

          print(result)


     except Exception as e:

          result = "Unable to click the " + module + " Icon, It causes Exception --> "+str(e)

          try:

               driver.save_screenshot(screenshot.get(ScreenshotName.moduleClick) + ".error.png")

               print("1. "+module+" click error screenshot is taken")

          except:
               print("1. "+module+" click error screenshot not taken")

          print(result)

          LogOperation.logError("result")

          navigatePermission = "FAIL"

     if navigatePermission=="PASS" :

          try:

               BasicOperation.scrollToElement(driver,element.get(ObjectName.subModuleIcon))

               BasicOperation.clickXpath(driver, element.get(ObjectName.subModuleIcon))

               try:

                    driver.save_screenshot(screenshot.get(ScreenshotName.subModuleClick) + ".info.png")

                    print("2. "+subModule+" click screenshot is taken")

               except:
                    print("2. "+subModule+" click screenshot not taken")



               navigatePermission = "PASS"

               result = "Clicked the " + subModule + " Icon"

               print(result)

               LogOperation.logInfo(result)

          except Exception as e:

               result = "Clicked the " + subModule + " Icon , It causes Exception --> "+str(e)

               try:

                    driver.save_screenshot(screenshot.get(ScreenshotName.moduleClick) + ".error.png")

                    print("2. " + subModule + " click screenshot is taken")

               except:
                    print("2. " + subModule + " click screenshot not taken")

               print(result)

               LogOperation.logError(result)

     else:
          navigatePermission = "FAIL"

     if navigatePermission == "PASS":

          try:

           BasicOperation.clickXpath(driver, element.get(ObjectName.screenIcon))

           try:

                driver.save_screenshot(screenshot.get(ScreenshotName.screenClick) + ".info.png")

                print("3. " + screen + " click screenshot is taken")

           except:
                print("3. " + screen + " click screenshot not taken")

           navigatePermission = "PASS"

           result = "clicked the " + screen + " Icon"

           print(result)


           LogOperation.logInfo(result)

          except Exception as e:
               result = " Unable to Click the " + subModule + " Icon, It causes the exception---> "+ str(e)

               try:

                    driver.save_screenshot(screenshot.get(ScreenshotName.screenClick) + ".error.png")

                    print("3. " + screen + " click screenshot is taken")

               except:
                    print("3. " + screen + " click screenshot not taken")

               print(result)

               LogOperation.logError(result)

     else:
          navigatePermission = "FAIL"

     if navigatePermission == "PASS":

          try:

               BasicOperation.clickXpath(driver, element.get(ObjectName.screenHeader))

               try:

                    driver.save_screenshot(screenshot.get(ScreenshotName.screenHeaderClick) + ".info.png")

                    print("4. screen header click  info screenshot is taken")

               except:
                    print("4. screen header click info screenshot not taken")

               navigatePermission = "PASS"

               result = "clicked the screen header"

               print(result)

               LogOperation.logInfo(result)

               navigatePermission = "PASS"

          except Exception as e:
               result = "Unable to click the screen header, It causes the exception---> "+ str(e)

               try:

                    driver.save_screenshot(screenshot.get(ScreenshotName.screenHeaderClick) + ".error.png")

                    print("4. screen header click error screenshot is taken")

               except:
                    print("4. screen header click error screenshot not taken")

               print(result)

               LogOperation.logError(result)


     else:
          navigatePermission = "FAIL"

     beforeCount=None

     if navigatePermission == "PASS":

          try:

               beforeCount=int(BasicOperation.totalCount(driver,element.get(ObjectName.totalCount)))



               result = "Checked the data count before add the "+screen+" detail "+str(beforeCount)+" "+screen+" details are  available in the screen"

               print(result)

               navigatePermission="PASS"

          except Exception as e:

               result= "Unable to get the number of record in the screen, It causes exception--"+str(e)

               print(result)

               navigatePermission ="FAIL"



     if navigatePermission == "PASS":

          try:
               BasicOperation.clickXpath(driver, element.get(ObjectName.add))

               try:

                    driver.save_screenshot(screenshot.get(ScreenshotName.addButtonClick) + ".info.png")

                    print("5. " +screen+ " Add button click info screenshot is taken")

               except:
                    print("5. " + screen + " Add button  click info screenshot not taken")



               navigatePermission = "PASS"

               result = "Clicked the Add button"

               print(result)

               LogOperation.logInfo(result)

          except Exception as e:

               result = "Unable to click the Add button, It causes the exception---> " + str(e)

               try:

                    driver.save_screenshot(screenshot.get(ScreenshotName.addButtonClick) + ".error.png")

                    print("5. " + screen + " Add button click error screenshot is taken")

               except:
                    print("5. " + screen + " Add button  click error screenshot not taken")

               print(result)

               LogOperation.logError(result)


     else:
          navigatePermission = "FAIL"

     if navigatePermission == "PASS":


          try:

               BasicOperation.sendKeysXpath(driver, element.get(ObjectName.name), value.get("name"))

               try:

                    driver.save_screenshot(screenshot.get(ScreenshotName.nameEnter) + ".info.png")

                    print("6. " + screen + " name enter info screenshot is taken")

               except:
                    print("6. " + screen + " name enter info screenshot not taken")

               navigatePermission = "PASS"

               result = "Entered the "+screen+ " name value "

               print(result)

               LogOperation.logInfo(result)

          except Exception as e:

               result = "Unable to enter the "+screen+" Name value, It causes the exception---> " + str(e)

               try:

                    driver.save_screenshot(screenshot.get(ScreenshotName.nameEnter) + ".error.png")

                    print("6. " + screen + " name enter error screenshot is taken")

               except:
                    print("6. " + screen + " name enter error screenshot not taken")

               print(result)

               LogOperation.logError(result)

     else:
          navigatePermission = "FAIL"

     if navigatePermission == "PASS":


          try:

               BasicOperation.sendKeysXpath(driver, element.get(ObjectName.description), value.get("description"))

               try:

                    driver.save_screenshot(screenshot.get(ScreenshotName.descriptionEnter) + ".info.png")

                    print("6. " + screen + " description enter info screenshot is taken")

               except:
                    print("6. " + screen + " descriptio  enter info screenshot not taken")

               navigatePermission = "PASS"

               result = "Entered the "+screen+ " description value "

               print(result)

               LogOperation.logInfo(result)

          except Exception as e:

               result = "Unable to enter the "+screen+" description value, It causes the exception---> " + str(e)

               try:

                    driver.save_screenshot(screenshot.get(ScreenshotName.descriptionEnter) + ".error.png")

                    print("6. " + screen + " description enter error screenshot is taken")

               except:
                    print("6. " + screen + " description enter error screenshot not taken")

               print(result)

               LogOperation.logError(result)

     else:
          navigatePermission = "FAIL"

     if navigatePermission == "PASS":

          try:

               BasicOperation.clickXpath(driver,element.get(ObjectName.defaultStatus))

               try:


                    driver.save_screenshot(screenshot.get(ScreenshotName.defaultStatus) + ".info.png")

                    print("7. " + screen + " default status click info screenshot is taken")

               except Exception as e:
                    print("7. " + screen + " default status click info screenshot not taken, Exceptio "+str(e))

               navigatePermission = "PASS"

               result =  screen + " default status button clicked "

               print(result)

               LogOperation.logInfo(result)

          except Exception as e:

               result = "Unable to click " + screen + "default status button, It causes the exception---> " + str(e)

               try:

                    driver.save_screenshot(screenshot.get(ScreenshotName.defaultStatus) + ".error.png")

                    print("7. " + screen + " default status click error screenshot is taken")

               except:
                    print("7. " + screen + " default status click error screenshot not taken")

               print(result)

               LogOperation.logError(result)

     else:
          navigatePermission = "FAIL"

     if navigatePermission == "PASS":


          try:

               BasicOperation.clickXpath(driver, element.get(ObjectName.addSubmit))

               try:

                    driver.save_screenshot(screenshot.get(ScreenshotName.addSubmitClick) + ".info.png")

                    print("7. " + screen + " add submit button click info screenshot is taken")

               except:
                    print("7. " + screen + " add submit button click info screenshot not taken")

               navigatePermission = "PASS"

               result = "Clicked the Add submit button"

               print(result)

               LogOperation.logInfo(result)

          except Exception as e:

               try:

                    driver.save_screenshot(screenshot.get(ScreenshotName.addSubmitClick) + ".error.png")

                    print("7. " + screen + " add submit button click error screenshot is taken")

               except:
                    print("7. " + screen + " add submit button click error screenshot not taken")

               result = "Unable to click the Add submit button, It causes the exception---> " + str(e)

               print(result)

               LogOperation.logError(result)

     else:
          navigatePermission = "FAIL"


     if navigatePermission=="PASS":

          driver.implicitly_wait(3)

          try:
               BasicOperation.clickXpath(driver,element.get(ObjectName.screenHeader))

               try:

                    driver.save_screenshot(screenshot.get(ScreenshotName.addPopupClose) + ".info.png")

                    print("8. " + screen + " add popup closed info screenshot is taken")

               except:
                    print("8. " + screen + " add popup closed info screenshot not taken")

               result="Add popup closed "

               print(result)

               navigatePermission="PASS"

               JDBC.name(value.get("name"))

          except Exception as e:

               try:
                    BasicOperation.clickXpath(driver,element.get(ObjectName.addPopupHeader))

                    result="Add popup is not closed"

                    print(result)

                    navigatePermission="FAIL"

                    try:

                         driver.save_screenshot(screenshot.get(ScreenshotName.addPopupClose) + ".error.png")

                         print("8. " + screen + " add popup close error screenshot is taken")

                    except:
                         print("8. " + screen + " add popup close error screenshot not taken")

               except:


                    result ="Undefined"
                    navigatePermission="FAIL"

                    print(result)

     afterCount=None

     if navigatePermission == "PASS":

          try:

               afterCount = int(BasicOperation.totalCount(driver, element.get(ObjectName.totalCount)))

               result = "Checked the data count after added the " + screen + " detail, "+str(afterCount)+" "+screen+" details are  available in the screen"

               print(result)

               navigatePermission = "PASS"

          except Exception as e:

               result = "Unable to get the number of record in the screen after added the data, It causes exception--" + str(e)

               print(result)

               navigatePermission = "FAIL"


     countIncreaseResult=None

     firstIndexResult=None

     '''

     if afterCount==beforeCount+1:

          countIncreaseResult=screen+" detail is added successfully, It added the data by one time"



          rows = driver.find_elements(By.TAG_NAME, "tr")

          firstRowText=rows[1].text

          textArray=firstRowText.split(' ')

          gridName = textArray[0]

          if gridName==value.get("name"):


               firstIndexResult="The added data is visible in the first index"

               print(firstIndexResult)

          else:
               firstIndexResult="The added data is not visible in the first index"

               print(firstIndexResult)


     elif afterCount>=beforeCount+1:
          countIncreaseResult=screen+" detail is added by more than one time"

     elif afterCount==beforeCount:
          countIncreaseResult=screen+" Add is not working"

     else:
          countIncreaseResult=screen+" Add is not working properly"

     print(countIncreaseResult)


     if navigatePermission=="PASS":

          try:
               BasicOperation.scrollToElement(driver,element.get(ObjectName.subModuleIcon))

               result = "Scrolled to "+subModule+" icon"

               navigatePermission = "PASS"

          except Exception as e:

               result="Unable to navigate into the "+subModule+", It causes Exception, ---> "+str(e)

               navigatePermission = "FAIL"



     if navigatePermission=="PASS":

          try:
               BasicOperation.clickXpath(driver, element.get(ObjectName.subModuleIcon))

               result = "Clicked the " + subModule + " icon"

               navigatePermission = "PASS"

          except Exception as e:

               result = "Unable to click the " + subModule + " Icon, It causes Exception, ---> " + str(e)

               navigatePermission = "FAIL"




     '''


