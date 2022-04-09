import time

from selenium.webdriver.common.by import By

from Utility import BrowserOperation, ScreenNavigate, BasicOperation

driver=BrowserOperation.launchLIMS()

driver.implicitly_wait(30)

BasicOperation.clickXpath(driver,"//span[text()='Registration']")

BasicOperation.clickXpath(driver,"//a[text()='Sample Registration']")

BasicOperation.clickXpath(driver,"//*[@id='content']/div[2]/div/div[2]/div/div/div/div[1]/div[2]/div[1]/div[1]/div[3]/div/button")

BasicOperation.clickXpath(driver,"//*[@id='nsampletypecode']/div/div[1]")

time.sleep(2)

BasicOperation.clickXpath(driver,"(//*[text()='Product'])[4]")

time.sleep(2)

BasicOperation.clickXpath(driver,"//*[@id='nregtypecode']/div/div[1]")

time.sleep(2)


BasicOperation.clickXpath(driver,"(//*[text()='Batch'])[3]")

BasicOperation.clickXpath(driver,"//*[@id='nregsubtypecode']/div/div[1]")

time.sleep(2)


BasicOperation.clickXpath(driver,"(//*[text()='EU'])[2]")

time.sleep(2)

BasicOperation.clickXpath(driver,"//*[text()='Submit']")

time.sleep(2)

BasicOperation.clickXpath(driver,"//button[@data-tip='Register']")

time.sleep(2)

BasicOperation.clickXpath(driver,"//div[@id='nrmsno']")

time.sleep(2)

BasicOperation.clickXpath(driver,"//div[text()='202200085']")


time.sleep(2)

BasicOperation.clickXpath(driver,"//div[@id='nproductcatcode']")

time.sleep(2)

BasicOperation.clickXpath(driver,"//div[text()='Albumins']")



time.sleep(2)

BasicOperation.clickXpath(driver,"//div[@id='nproductcode']")

time.sleep(2)

BasicOperation.clickXpath(driver,"//div[text()='Albumin 25% (250g/L)']")

time.sleep(2)


BasicOperation.clickXpath(driver,"/html/body/div[5]/div/div/div[2]/div/div/form/div[1]/div[1]/div[4]/div/div/div/div/div")

BasicOperation.clickXpath(driver,"//td[text()='Baxalta US Inc.']")

BasicOperation.clickXpath(driver,"//label[text()='All Test']")

BasicOperation.clickXpath(driver,"(//a[text()='Component'])[2]")




time.sleep(2)
BasicOperation.clickXpath(driver,"//div[@id='ncomponentcode']")
time.sleep(2)
BasicOperation.clickXpath(driver,"//div[text()='Manufacturers Protocol']")


time.sleep(2)
BasicOperation.sendKeysXpath(driver,"//input[@id='smanuflotno']","1001")

time.sleep(2)
BasicOperation.clickXpath(driver,"//div[@id='nstorageconditioncode']")
time.sleep(2)
BasicOperation.clickXpath(driver,"//div[text()='-80°C']")


time.sleep(2)
BasicOperation.clickXpath(driver,"//div[@id='nstoragelocationcode']")
time.sleep(2)
BasicOperation.clickXpath(driver,"//div[text()='CR005']")


time.sleep(2)
BasicOperation.sendKeysXpath(driver,"//input[@name='nnoofcontainer']","10")

time.sleep(2)
BasicOperation.clickXpath(driver,"//*[text()='Save']")

time.sleep(2)

BasicOperation.clickXpath(driver,"//a[text()='Test']")


time.sleep(2)

BasicOperation.clickXpath(driver,"//div[@tabindex='0'][@aria-labelledby='Select']")

BasicOperation.clickXpath(driver,"//span[text()='Citrate - Manufacturer']")


time.sleep(2)
BasicOperation.clickXpath(driver,"//*[text()='Save']")


time.sleep(2)
BasicOperation.clickXpath(driver,"//*[text()='Save']")

time.sleep(2)
BasicOperation.clickXpath(driver,"//a[@data-tip='Accept']")