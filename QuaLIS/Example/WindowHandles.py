from Utility import BrowserOperation

driver=BrowserOperation.launchLIMS()

driver.execute_script("window.open()")
handles=driver.window_handles
handle=handles[1]
print(handle)
driver.switch_to.window(handle)
print(driver.title)
