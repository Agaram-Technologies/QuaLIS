from selenium.webdriver.common.by import By


def auditDate(driver,index):
    driver.find_element(By.XPATH, "//tbody[@role='presentation']/tr[{}]/td[2]".format(index))


def auditAction(driver, index):
    driver.find_element(By.XPATH, "//tbody[@role='presentation']/tr[{}]/td[3]".format(index))

def auditComment(driver, index):
    driver.find_element(By.XPATH, "//tbody[@role='presentation']/tr[{}]/td[4]".format(index))

def userName(driver, index):
    driver.find_element(By.XPATH, "//tbody[@role='presentation']/tr[{}]/td[5]".format(index))

def userRole(driver, index):
    driver.find_element(By.XPATH, "//tbody[@role='presentation']/tr[{}]/td[6]".format(index))


def actionType(driver, index):
    driver.find_element(By.XPATH, "//tbody[@role='presentation']/tr[{}]/td[7]".format(index))

def moduleName(driver, index):
    moduleName=driver.find_element(By.XPATH, "//tbody[@role='presentation']/tr[{}]/td[8]".format(index))
    return moduleName

def formName(driver, index):
    driver.find_element(By.XPATH, "//tbody[@role='presentation']/tr[{}]/td[9]".format(index))

def esignComments(driver, index):
    driver.find_element(By.XPATH, "//tbody[@role='presentation']/tr[{}]/td[10]".format(index))