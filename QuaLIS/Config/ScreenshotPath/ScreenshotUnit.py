from configparser import ConfigParser

from Config.ScreenshotPath import ScreenshotName
from Utility import BasicOperation

screenshotPath=BasicOperation.projectDirectory()+"\\Report\\Screenshot\\Unit\\UnitAddAllFieldDefaultYes\\"

def screenshotUnitAddAllFieldDefaultYes():
    screenshot={}
    screenshot.update({ScreenshotName.moduleClick:screenshotPath+"1.Master Click"})

    screenshot.update({ScreenshotName.subModuleClick: screenshotPath+"2.Base Master Click"})

    screenshot.update({ScreenshotName.screenClick: screenshotPath+"3. Unit screen Click"})

    screenshot.update({ScreenshotName.screenHeaderClick: screenshotPath+"4. Unit screen header Click"})

    screenshot.update({ScreenshotName.addButtonClick: screenshotPath+"5. Add button Click"})

    screenshot.update({ScreenshotName.nameEnter: screenshotPath+"6. Enter name detail"})

    screenshot.update({ScreenshotName.descriptionEnter: screenshotPath+"7. Enter description detail"})

    screenshot.update({ScreenshotName.defaultStatus: screenshotPath + "8. Default Status"})

    screenshot.update({ScreenshotName.addSubmitClick:screenshotPath+ "9. Click add submit button"})

    screenshot.update({ScreenshotName.addPopupClose: screenshotPath+"10. Add popup closed"})

    return  screenshot








