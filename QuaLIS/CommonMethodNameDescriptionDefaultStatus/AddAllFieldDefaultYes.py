from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Config import ObjectName
from Utility import BasicOperation, LogOperation, BrowserOperation


def addFieldValueDefaultYes(driver,element,value):



     value = dict(value)

     element = dict(element)

     module = element.get(ObjectName.module)

     subModule = element.get(ObjectName.subModule)

     screen = element.get(ObjectName.screen)

     navigatePermission="FAIL"

     try:

          BasicOperation.clickXpath(driver, element.get(ObjectName.moduleIcon))

          navigatePermission = "PASS"

          result = "Clicked the "+module+" Icon"

          print(result)

          LogOperation.logInfo(result)

     except Exception as e:

          result = "Unable to click the " + module + " Icon, It causes Exception --> "+str(e)

          print(result)

          LogOperation.logError("result")

          navigatePermission = "FAIL"

     if navigatePermission=="PASS" :

          try:

               BasicOperation.scrollToElement(driver,element.get(ObjectName.subModuleIcon))


               BasicOperation.clickXpath(driver, element.get(ObjectName.subModuleIcon))

               navigatePermission = "PASS"

               result = "Clicked the " + subModule + " Icon"

               print(result)

               LogOperation.logInfo(result)

          except Exception as e:

               result = "Clicked the " + subModule + " Icon , It causes Exception --> "+str(e)

               print(result)

               LogOperation.logError(result)

     else:
          navigatePermission = "FAIL"

     if navigatePermission == "PASS":

          try:

           BasicOperation.clickXpath(driver, element.get(ObjectName.screenIcon))

           navigatePermission = "PASS"

           result = "clicked the " + screen + " Icon"

           print(result)

           LogOperation.logInfo(result)

          except Exception as e:
               result = " Unable to Click the " + subModule + " Icon, It causes the exception---> "+ str(e)

               print(result)

               LogOperation.logError(result)

     else:
          navigatePermission = "FAIL"

     if navigatePermission == "PASS":

          try:

               BasicOperation.clickXpath(driver, element.get(ObjectName.screenHeader))

               navigatePermission = "PASS"

               result = "clicked the screen header"

               print(result)

               LogOperation.logInfo(result)

               navigatePermission = "PASS"

          except Exception as e:
               result = "Unable to click the screen header, It causes the exception---> "+ str(e)

               print(result)

               LogOperation.logError(result)


     else:
          navigatePermission = "FAIL"

     if navigatePermission == "PASS":

          try:
               BasicOperation.clickXpath(driver, element.get(ObjectName.add))

               navigatePermission = "PASS"

               result = "Clicked the Add button"

               print(result)

               LogOperation.logInfo(result)

          except Exception as e:

               result = "Unable to click the Add button, It causes the exception---> " + str(e)

               print(result)

               LogOperation.logError(result)


     else:
          navigatePermission = "FAIL"

     if navigatePermission == "PASS":


          try:

               BasicOperation.sendKeysXpath(driver, element.get(ObjectName.name), value.get("name"))

               navigatePermission = "PASS"

               result = "Entered the "+screen+ " name value "

               print(result)

               LogOperation.logInfo(result)

          except Exception as e:

               result = "Unable to enter the "+screen+"Name value, It causes the exception---> " + str(e)

               print(result)

               LogOperation.logError(result)

     else:
          navigatePermission = "FAIL"

     if navigatePermission == "PASS":


          try:

               BasicOperation.sendKeysXpath(driver, element.get(ObjectName.description), value.get("description"))

               navigatePermission = "PASS"

               result = "Entered the "+screen+ " description value "

               print(result)

               LogOperation.logInfo(result)

          except Exception as e:

               result = "Unable to enter the "+screen+"description value, It causes the exception---> " + str(e)

               print(result)

               LogOperation.logError(result)

     else:
          navigatePermission = "FAIL"

     if navigatePermission == "PASS":


          try:

               BasicOperation.clickXpath(driver, element.get(ObjectName.addSubmit))

               navigatePermission = "PASS"

               result = "Clicked the Add submit button"

               print(result)

               LogOperation.logInfo(result)

          except Exception as e:

               result = "Unable to click the Add submit button, It causes the exception---> " + str(e)

               print(result)

               LogOperation.logError(result)

     else:
          navigatePermission = "FAIL"


     if navigatePermission=="PASS":

          driver.implicitly_wait(3)

          try:
               BasicOperation.clickXpath(driver,element.get(ObjectName.screenHeader))

               result="Add popup closed "

               print(result)

               navigatePermission="PASS"

          except Exception as e:

               try:
                    BasicOperation.clickXpath(driver,element.get(ObjectName.addPopupHeader))

                    result="Add popup is not closed"

                    print(result)

                    navigatePermission="FAIL"

               except:
                    result ="Undefined"
                    navigatePermission="FAIL"

                    print(result)



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







