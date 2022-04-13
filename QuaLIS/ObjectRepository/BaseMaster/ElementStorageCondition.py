from Config import ObjectName


pin = "//a[@class='text-center nav-link']"

masterIcon="//a[@data-rb-event-key='MenuId_1']"

baseMasterIcon="//span[text()='Base Master']"

storageConditionIcon="//a[@href='#/storageCondition']"

storageConditionAdd="//button[@data-tip='Add']"

storageConditionRefresh="//button[@data-tip='Refresh']"

storageConditionDownloadPDF="//button[@data-tip='Download PDF']"

storageConditionDownloadExcel="//button[@data-tip='Download Excel']"

storageConditionName="//input[@id='sstorageconditionname'][@name='sstorageconditionname']"

storageConditionDescription="//textarea[@id='sdescription'][@name='sdescription']"

storageConditionAddSubmit="//button[text()='Save']"

storageConditionAddCancel="//button[text()='Cancel']"

storageConditionEditSubmit="//button[text()='Save']"

storageConditionEditCancel="//button[text()='Cancel']"

storageConditionNameList="/html/body/div[1]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[3]/div/div[1]/table/tbody/tr/td[1]"

storageConditionDescriptionList="//tbody[@role='presentation']/tr/td[2]"

storageConditionDefaultStatusList="//tbody[@role='presentation']/tr/td[3]"

storageConditionEditList="//tbody[@role='presentation']/tr/td[4]/a/span[1]"

storageConditionDeleteList="//tbody[@role='presentation']/tr/td[4]/a/span[2]"

storageConditionNameFilter="(//span[@class='k-icon k-i-more-vertical'])[1]"

storageConditionDefaultStatus="/html/body/div[5]/div/div/div[2]/div/div/form/div/div[3]/div/label"

storageConditionDefaultStatusToggle="//input[@name='ndefaultstatus' and @type='checkbox']"

storageConditionCount="//div[@class='k-pager-info k-label']"

storageConditionScreenHeader="//*[@class='navbar-brand']/h2"

storageConditionAddPopupHeader="//div[@class='header-primary flex-grow-1 modal-title h4' and @id='add-user']"

module="Master"

subModule="Base Master"

screen="storage Condition"


def elementstorageCondition():

    storageCondition={}

    storageCondition.update({ObjectName.moduleIcon:masterIcon})

    storageCondition.update({ObjectName.subModuleIcon:baseMasterIcon})

    storageCondition.update({ObjectName.screenIcon:storageConditionIcon})

    storageCondition.update({ObjectName.add:storageConditionAdd})

    storageCondition.update({ObjectName.name: storageConditionName})

    storageCondition.update({ObjectName.description:storageConditionDescription})

    storageCondition.update({ObjectName.addSubmit:storageConditionAddSubmit})

    storageCondition.update({ObjectName.addCancel:storageConditionAddCancel})

    storageCondition.update({ObjectName.screenHeader:storageConditionScreenHeader})

    storageCondition.update({ObjectName.module:module})

    storageCondition.update({ObjectName.subModule:subModule})

    storageCondition.update({ObjectName.screen:screen})

    storageCondition.update({ObjectName.addPopupHeader:storageConditionAddPopupHeader})


    return storageCondition


