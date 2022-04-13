from Config import ObjectName




pin = "//a[@class='text-center nav-link']"

masterIcon="//a[@data-rb-event-key='MenuId_1']"

baseMasterIcon="//span[text()='Base Master']"

unitOfMeasurementIcon="//a[@href='#/unit']"

unitAdd="//button[@data-tip='Add']"

unitRefresh="//button[@data-tip='Refresh']"

unitDownloadPDF="//button[@data-tip='Download PDF']"

unitDownloadExcel="//button[@data-tip='Download Excel']"

unitName="//input[@id='sunitname'][@name='sunitname']"

unitDescription="//textarea[@id='sdescription'][@name='sdescription']"

unitAddSubmit="//button[text()='Save']"

unitAddCancel="//button[text()='Cancel']"

unitEditSubmit="//button[text()='Save']"

unitEditCancel="//button[text()='Cancel']"

unitNameList="/html/body/div[1]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[3]/div/div[1]/table/tbody/tr/td[1]"

unitDescriptionList="//tbody[@role='presentation']/tr/td[2]"

unitDefaultStatusList="//tbody[@role='presentation']/tr/td[3]"

UnitEditList="//tbody[@role='presentation']/tr/td[4]/a/span[1]"

unitDeleteList="//tbody[@role='presentation']/tr/td[4]/a/span[2]"

unitNameFilter="(//span[@class='k-icon k-i-more-vertical'])[1]"

unitDefaultStatus="/html/body/div[5]/div/div/div[2]/div/div/form/div/div[3]/div/label"

unitDefaultStatusToggle="//input[@name='ndefaultstatus' and @type='checkbox']"

unitCount="//div[@class='k-pager-info k-label']"

unitScreenHeader="//*[@class='navbar-brand']/h2"

unitAddPopupHeader="//div[@class='header-primary flex-grow-1 modal-title h4' and @id='add-user']"

module="Master"

subModule="Base Master"

screen="Unit"


def elementUnit():

    unit={}

    unit.update({ObjectName.moduleIcon:masterIcon})

    unit.update({ObjectName.subModuleIcon:baseMasterIcon})

    unit.update({ObjectName.screenIcon:unitOfMeasurementIcon})

    unit.update({ObjectName.add:unitAdd})

    unit.update({ObjectName.name: unitName})

    unit.update({ObjectName.description:unitDescription})

    unit.update({ObjectName.addSubmit:unitAddSubmit})

    unit.update({ObjectName.addCancel:unitAddCancel})

    unit.update({ObjectName.screenHeader:unitScreenHeader})

    unit.update({ObjectName.module:module})

    unit.update({ObjectName.subModule:subModule})

    unit.update({ObjectName.screen:screen})

    unit.update({ObjectName.addPopupHeader:unitAddPopupHeader})

    unit.update({ObjectName.moduleIcon:masterIcon})

    unit.update({ObjectName.moduleIcon:masterIcon})

    return unit



