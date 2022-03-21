from TestCoverage import TestCoverageUnit
from Utility import BrowserOperation, BasicOperation

name="murali"


driver=BrowserOperation.launchLIMS()

#TestCoverageUnit.unitAdd(driver,name,"dd")

TestCoverageUnit.unitDelete(driver,name)



